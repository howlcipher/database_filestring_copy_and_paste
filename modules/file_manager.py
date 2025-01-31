import shutil

class FileManager:
    def __init__(self, config, logger):
        """
        Initialize FileManager with configuration and logger instance.
        
        Args:
        - config (Config): Config instance containing file management configuration.
        - logger (Logger): Logger instance.
        """
        self.config = config
        self.logger = logger

    def copy_files(self, df, file_column):
        """
        Copy files based on DataFrame and file column name.
        
        Args:
        - df (pd.DataFrame): DataFrame containing file paths.
        - file_column (str): Name of the column containing file paths.
        """
        destination_directory = self.config.get_destination_directory()

        for index, row in df.iterrows():
            file_path = row[file_column]
            try:
                shutil.copy(file_path, destination_directory)
                self.logger.info(f'File copied: {file_path}')
            except Exception as e:
                self.logger.error(f'Error copying file {file_path}: {e}')
