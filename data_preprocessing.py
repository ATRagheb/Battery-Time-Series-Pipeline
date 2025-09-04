import pandas as pd
from logger import logger

def drop_specific_values(df, column, value):
    """
    Drop rows with specific value in a column
    
    Args:
        df (pd.DataFrame): DataFrame to process
        column (str): Column name to check
        value (any): Value to drop
        
    Returns:
        pd.DataFrame: DataFrame with rows dropped
    """
    dropped_indices = df[df[column] == value].index
    df_cleaned = df.drop(dropped_indices)
    logger.info(f"Removed {len(dropped_indices)} rows with value {value} in {column} column")
    return df_cleaned

def remove_duplicates(df, subset_columns):
    """
    Remove duplicate rows based on subset of columns
    
    Args:
        df (pd.DataFrame): DataFrame to process
        subset_columns (list): List of column names to check for duplicates
        
    Returns:
        pd.DataFrame: DataFrame with duplicates removed
    """
    df["is_duplicate"] = df.duplicated(subset=subset_columns, keep=False)
    logger.info(f"Found {df['is_duplicate'].sum()} duplicate rows")
    
    df_filtered = df[df["is_duplicate"] == False]
    logger.info(f"Removed {df['is_duplicate'].sum()} duplicate rows")
    
    df_filtered = df_filtered.drop(columns=["is_duplicate"])
    return df_filtered

def convert_data_types(df, type_conversions):
    """
    Convert data types of columns
    
    Args:
        df (pd.DataFrame): DataFrame to process
        type_conversions (dict): Dictionary mapping column names to data types
        
    Returns:
        pd.DataFrame: DataFrame with converted data types
    """
    for column, dtype in type_conversions.items():
        if column in df.columns:
            df[column] = df[column].astype(dtype)
    
    return df

def convert_timestamp(df, timestamp_column):
    """
    Convert timestamp column to datetime
    
    Args:
        df (pd.DataFrame): DataFrame to process
        timestamp_column (str): Name of timestamp column
        
    Returns:
        pd.DataFrame: DataFrame with timestamp column converted
    """
    df[timestamp_column] = pd.to_datetime(df[timestamp_column])
    return df

def fill_nulls(df, fill_strategy):
    """
    Fill null values in DataFrame
    
    Args:
        df (pd.DataFrame): DataFrame to process
        fill_strategy (dict): Dictionary mapping column names to fill strategies
                             (e.g., {'column_name': 'median'})
        
    Returns:
        pd.DataFrame: DataFrame with nulls filled
    """
    for column, strategy in fill_strategy.items():
        if column in df.columns:
            if strategy == 'median':
                df[column].fillna(df[column].median(), inplace=True)
            elif strategy == 'mean':
                df[column].fillna(df[column].mean(), inplace=True)
            elif strategy == 'mode':
                df[column].fillna(df[column].mode()[0], inplace=True)
            elif isinstance(strategy, (int, float, str)):
                df[column].fillna(strategy, inplace=True)
    
    logger.info("Filled null values according to specified strategies")
    return df

def extract_time_features(df, timestamp_column):
    """
    Extract time features from timestamp column
    
    Args:
        df (pd.DataFrame): DataFrame to process
        timestamp_column (str): Name of timestamp column
        
    Returns:
        pd.DataFrame: DataFrame with time features added
    """
    df['hour'] = df[timestamp_column].dt.hour
    df['day'] = df[timestamp_column].dt.day
    df['month'] = df[timestamp_column].dt.month
    df['year'] = df[timestamp_column].dt.year
    df['dayofweek'] = df[timestamp_column].dt.dayofweek
    
    return df