import json

class Config:
    def __init__(self, config_path):
        """
        Initialize Config with configuration from config.json.
        
        Args:
        - config_path (str): Path to the configuration file (config.json).
        """
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        """
        Load configuration from config.json.
        """
        with open(self.config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def get_database_config(self):
        """
        Get database configuration from loaded config.
        
        Returns:
        - dict: Database configuration.
        """
        return self.config['database']

    def get_destination_directory(self):
        """
        Get destination directory from loaded config.
        
        Returns:
        - str: Destination directory path.
        """
        return self.config['destination_directory']
