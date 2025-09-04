import logging

def setup_logger(name='battery_pipeline', log_file='battery_processing.log', level=logging.INFO):
    """
    Set up and configure a logger instance that can be imported and used across multiple files
    
    Args:
        name (str): Name of the logger
        log_file (str): File to write logs to
        level (int): Logging level
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create handlers
    # file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()
    
    # Create formatter and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    # logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create a default logger instance
logger = setup_logger()