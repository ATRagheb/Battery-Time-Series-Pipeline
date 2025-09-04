import pandas as pd
from logger import logger

def load_battery_data(file_path='data/measurements_coding_challenge.csv', delimiter=';'):
    """
    Load battery data from CSV file
    
    Args:
        file_path (str): Path to the CSV file
        delimiter (str): Delimiter used in the CSV file
        
    Returns:
        pd.DataFrame: Loaded battery data
    """
    logger.info('Loading battery data from file')
    battery_df = pd.read_csv(file_path, delimiter=delimiter)
    logger.info(f'Loaded battery data with {len(battery_df)} records')
    return battery_df

