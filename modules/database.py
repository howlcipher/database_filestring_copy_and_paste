from sqlalchemy import create_engine, text
import pandas as pd

class DatabaseManager:
    def __init__(self, config, logger):
        """
        Initialize DatabaseManager with configuration and logger instance.
        
        Args:
        - config (Config): Config instance containing database configuration.
        - logger (Logger): Logger instance.
        """
        self.config = config
        self.logger = logger
        self.engine = None  # SQLAlchemy engine will be initialized in connect method
        self.connection = None  # Initialize connection attribute

    def connect(self):
        """
        Connect to the database using SQLAlchemy Engine.
        """
        try:
            db_config = self.config.get_database_config()
            server = db_config['server']
            database = db_config['database']

            # SQLAlchemy connection string for SQL Server with Windows Authentication
            connection_string = f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
            self.engine = create_engine(connection_string)
            self.connection = self.engine.connect()  # Open connection
            self.logger.info('Database connected successfully.')
        except Exception as e:
            self.logger.error(f'Error connecting to database: {e}')
            raise

    def run_query(self, query_str):
        """
        Execute SQL query using SQLAlchemy Engine and return results as a pandas DataFrame.
        
        Args:
        - query_str (str): SQL query string.
        
        Returns:
        - pd.DataFrame: Result set of the SQL query.
        """
        try:
            if self.engine is None or self.connection is None:
                self.connect()

            result = self.connection.execute(text(query_str))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())

            self.logger.info('Query executed successfully.')
            return df
        except Exception as e:
            self.logger.error(f'Error running query: {e}')
            raise

    def close_connection(self):
        """
        Close the database connection.
        """
        try:
            if self.connection is not None:
                self.connection.close()
                self.logger.info('Database connection closed.')
        except Exception as e:
            self.logger.error(f'Error closing database connection: {e}')
            raise
