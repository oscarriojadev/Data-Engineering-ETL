# csv_merger_batch.py

import pandas as pd
import os
import glob

def read_csv(file_path):
    """
    Read a CSV file and return the data as a Pandas DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Data from the CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def merge_csv_files(file_paths, on=None, how='outer'):
    """
    Merge multiple CSV files into a single DataFrame.

    Parameters:
    file_paths (list): List of paths to the CSV files.
    on (str): Column to join on. If None, concatenate the DataFrames.
    how (str): Type of merge to be performed ('left', 'right', 'outer', 'inner').

    Returns:
    pd.DataFrame: Merged data.
    """
    data_frames = [read_csv(file_path) for file_path in file_paths]
    if on is None:
        merged_data = pd.concat(data_frames, ignore_index=True)
    else:
        merged_data = data_frames[0]
        for df in data_frames[1:]:
            merged_data = pd.merge(merged_data, df, on=on, how=how)
    return merged_data

def save_to_csv(data, file_path):
    """
    Save the merged data to a CSV file.

    Parameters:
    data (pd.DataFrame): Data to save.
    file_path (str): Path to the output CSV file.
    """
    data.to_csv(file_path, index=False)

def main():
    # Example usage
    input_directory = 'path_to_your_csv_files'
    output_file_path = 'merged_data.csv'

    # Get all CSV files in the input directory
    csv_files = glob.glob(os.path.join(input_directory, '*.csv'))

    # Merge the CSV files
    merged_data = merge_csv_files(csv_files)

    # Save the merged data to a CSV file
    save_to_csv(merged_data, output_file_path)
    print(f'Merged data saved to {output_file_path}')

if __name__ == '__main__':
    main()
