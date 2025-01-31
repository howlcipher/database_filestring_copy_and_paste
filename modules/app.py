from .config import Config
from .database import DatabaseManager
from .file_manager import FileManager
from .log import Logger

class App:
    def __init__(self, config_path):
        """
        Initialize the App with the provided configuration path.
        
        Args:
        - config_path (str): Path to the configuration file (config.json).
        """
        self.config = Config(config_path)
        self.logger = Logger()  # Assuming default log file 'app.log'
        self.db_manager = DatabaseManager(self.config, self.logger)
        self.file_manager = FileManager(self.config, self.logger)
        
    def run(self):
        """
        Run the application.
        """
        try:
            # Example query string
            query_str = """
                SELECT DISTINCT '\\\\alp-synnas-01\\RecordingRetrieval\\' 
                + REPLACE(SUBSTRING([File_Path], CHARINDEX('>', [File_Path]) + 1, 
                LEN([File_Path]) - CHARINDEX('>', [File_Path]) - 4), '/', '\\\\') 
                + 'opus' AS file_path 
                FROM [I3Custom].[dbo].[CallRecordingsExportedBeforeGenesysCloud] 
                WHERE recording_ID = '95736e17-b764-d0ae-8125-4e39f8900001';
            """
            
            # Run SQL query and get DataFrame
            df = self.db_manager.run_query(query_str)
            
            # Load configuration to get file column name
            file_column = self.config.get_database_config()['file_column']
            
            # Copy files based on query result
            self.file_manager.copy_files(df, file_column)
            
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            # Ensure database connection is closed even if an exception occurs
            self.db_manager.close_connection()

# Entry point for the application
if __name__ == "__main__":
    config_path = 'config.json'
    app = App(config_path)
    app.run()
