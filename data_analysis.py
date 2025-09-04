import pandas as pd
from logger import logger

def calculate_hourly_aggregations(df, group_column='hour', agg_columns=None):
    """
    Calculate aggregations by hour
    
    Args:
        df (pd.DataFrame): DataFrame to process
        group_column (str): Column to group by (default: 'hour')
        agg_columns (dict): Dictionary mapping column names to aggregation functions
                           (e.g., {'grid_purchase': 'sum', 'grid_feedin': 'sum'})
        
    Returns:
        pd.DataFrame: DataFrame with hourly aggregations
    """
    if agg_columns is None:
        agg_columns = {
            'grid_purchase': 'sum',
            'grid_feedin': 'sum'
        }
    
    hourly_aggregations = df.groupby(group_column).agg(agg_columns).reset_index()
    logger.info(f'Calculated aggregations by {group_column}')
    return hourly_aggregations

def find_max_value_hour(df, column, group_column='hour'):
    """
    Find the hour with the maximum value for a specific column
    
    Args:
        df (pd.DataFrame): DataFrame to process
        column (str): Column to find maximum value for
        group_column (str): Column that contains the hour information
        
    Returns:
        int: Hour with maximum value
    """
    max_value_hour = df.loc[df[column].idxmax(), group_column]
    logger.info(f'Hour with highest {column}: {max_value_hour}')
    return max_value_hour

def add_max_indicator(df, indicator_column, value_column, max_value):
    """
    Add a column indicating if this is the row with maximum value
    
    Args:
        df (pd.DataFrame): DataFrame to process
        indicator_column (str): Name of the new indicator column
        value_column (str): Column to check for maximum value
        max_value: Value to compare against
        
    Returns:
        pd.DataFrame: DataFrame with indicator column added
    """
    df[indicator_column] = df[value_column] == max_value
    return df

def add_max_hour_indicator(df, hour_column, max_hour, indicator_column='is_max_feedin_hour'):
    """
    Add a column indicating if this is the hour with maximum value
    
    Args:
        df (pd.DataFrame): DataFrame to process
        hour_column (str): Column containing hour values
        max_hour (int): Hour with maximum value
        indicator_column (str): Name of the new indicator column
        
    Returns:
        pd.DataFrame: DataFrame with indicator column added
    """
    df[indicator_column] = df[hour_column] == max_hour
    return df

def save_to_csv(df, output_file='output.csv', index=False):
    """
    Save DataFrame to CSV file
    
    Args:
        df (pd.DataFrame): DataFrame to save
        output_file (str): Path to output file
        index (bool): Whether to include index in output
        
    Returns:
        str: Path to output file
    """
    df.to_csv(output_file, index=index)
    logger.info(f'Wrote transformed data to {output_file}')
    return output_file