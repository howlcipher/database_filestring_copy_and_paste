import logging

class Logger:
    def __init__(self, log_file='app.log'):
        """
        Initialize the Logger with the specified log file.
        
        Args:
        - log_file (str): Path to the log file.
        """
        self.log_file = log_file
        self.setup_logging()

    def setup_logging(self):
        """
        Setup logging configuration.
        """
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

    def get_logger(self, name):
        """
        Get a logger with the specified name.
        
        Args:
        - name (str): Name of the logger.
        
        Returns:
        - logging.Logger: Configured logger instance.
        """
        return logging.getLogger(name)

    def debug(self, message):
        """
        Log a debug message.
        
        Args:
        - message (str): Debug message to log.
        """
        logging.debug(message)

    def info(self, message):
        """
        Log an info message.
        
        Args:
        - message (str): Info message to log.
        """
        logging.info(message)

    def warning(self, message):
        """
        Log a warning message.
        
        Args:
        - message (str): Warning message to log.
        """
        logging.warning(message)

    def error(self, message):
        """
        Log an error message.
        
        Args:
        - message (str): Error message to log.
        """
        logging.error(message)

    def critical(self, message):
        """
        Log a critical message.
        
        Args:
        - message (str): Critical message to log.
        """
        logging.critical(message)
