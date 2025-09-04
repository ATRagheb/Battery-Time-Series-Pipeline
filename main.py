from logger import logger
from data_loader import load_battery_data
from data_preprocessing import (
    drop_specific_values, remove_duplicates, convert_data_types,
    convert_timestamp, fill_nulls, extract_time_features
)
from data_analysis import calculate_hourly_aggregations



def main():
    """Main function to run the battery data processing pipeline"""
    logger.info('Starting battery data processing pipeline')
    
    # Configuration
    data_file = 'data/measurements_coding_challenge.csv'
    output_file = 'outputs/output.csv'
    delimiter = ';'
    
    # Load data
    battery_df = load_battery_data(file_path=data_file, delimiter=delimiter)
    
    # Preview data
    logger.info('Preview of the battery data:')
    logger.info(f'\n{battery_df.head()}')
    logger.info(battery_df.info())
    
    # Drop specific values
    battery_df = drop_specific_values(battery_df, 'grid_purchase', 'Dev test')
    
    # Remove duplicates
    battery_df_filtered = remove_duplicates(battery_df, ['timestamp', 'serial'])
    
    # Convert data types
    battery_df_filtered = convert_data_types(battery_df_filtered, {'grid_purchase': float, 'grid_feedin': float})
    
    # Convert timestamp
    battery_df_filtered = convert_timestamp(battery_df_filtered, 'timestamp')
    
    # Fill nulls
    battery_df_filtered = fill_nulls(battery_df_filtered, {'grid_purchase': 'median','grid_feedin': 'median'})
    
    # Extracting hour 
    battery_df_filtered = extract_time_features(battery_df_filtered, 'timestamp')
    
    # Calculate hourly aggregations
    hourly_aggregations = calculate_hourly_aggregations(battery_df_filtered, group_column='hour', agg_columns={'grid_purchase': 'sum', 'grid_feedin': 'sum'})

    # Find hour with highest grid_feedin
    max_feedin_hour = hourly_aggregations.loc[hourly_aggregations['grid_feedin'].idxmax(), 'hour']
    logger.info(f'Hour with highest grid_feedin: {max_feedin_hour}')
    
    # Add indicator for max feedin hour
    hourly_aggregations['is_max_feedin_hour'] = hourly_aggregations['hour'] == max_feedin_hour
    
    logger.info('Hourly aggregations:')
    logger.info(f'\n{hourly_aggregations.head()}')
    
    # Saving the aggregation dataframe
    hourly_aggregations.to_csv(output_file)
    logger.info(f'Wrote transformed data to {output_file}')


if __name__ == "__main__":
    main()
