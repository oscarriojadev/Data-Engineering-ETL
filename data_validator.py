# data_validator.py

import pandas as pd
import numpy as np

def check_data_types(data, expected_types):
    """
    Check if the data types of the columns match the expected types.

    Parameters:
    data (pd.DataFrame): Input data.
    expected_types (dict): Dictionary of expected data types for each column.

    Returns:
    bool: True if all data types match, False otherwise.
    """
    for column, expected_type in expected_types.items():
        if column in data.columns:
            if data[column].dtype != expected_type:
                print(f'Data type mismatch for column {column}. Expected {expected_type}, found {data[column].dtype}')
                return False
        else:
            print(f'Column {column} not found in the data')
            return False
    return True

def check_missing_values(data, max_missing_ratio=0.1):
    """
    Check for missing values in the data.

    Parameters:
    data (pd.DataFrame): Input data.
    max_missing_ratio (float): Maximum allowed ratio of missing values.

    Returns:
    bool: True if the missing values are within the limit, False otherwise.
    """
    missing_values = data.isnull().sum()
    total_values = len(data)
    missing_ratio = missing_values / total_values
    for column, ratio in missing_ratio.items():
        if ratio > max_missing_ratio:
            print(f'Column {column} has {ratio * 100:.2f}% missing values, which exceeds the limit of {max_missing_ratio * 100:.2f}%')
            return False
    return True

def check_duplicates(data):
    """
    Check for duplicate rows in the data.

    Parameters:
    data (pd.DataFrame): Input data.

    Returns:
    bool: True if no duplicates are found, False otherwise.
    """
    duplicates = data.duplicated()
    if duplicates.any():
        print(f'Found {duplicates.sum()} duplicate rows')
        return False
    return True

def check_custom_rules(data, custom_rules):
    """
    Check custom validation rules on the data.

    Parameters:
    data (pd.DataFrame): Input data.
    custom_rules (dict): Dictionary of custom validation rules.

    Returns:
    bool: True if all custom rules are satisfied, False otherwise.
    """
    for column, rule in custom_rules.items():
        if column in data.columns:
            if not rule(data[column]):
                print(f'Custom rule failed for column {column}')
                return False
        else:
            print(f'Column {column} not found in the data')
            return False
    return True

def validate_data(data, expected_types, max_missing_ratio=0.1, custom_rules=None):
    """
    Validate the data based on the specified rules.

    Parameters:
    data (pd.DataFrame): Input data.
    expected_types (dict): Dictionary of expected data types for each column.
    max_missing_ratio (float): Maximum allowed ratio of missing values.
    custom_rules (dict): Dictionary of custom validation rules.

    Returns:
    bool: True if all validations pass, False otherwise.
    """
    if not check_data_types(data, expected_types):
        return False
    if not check_missing_values(data, max_missing_ratio):
        return False
    if not check_duplicates(data):
        return False
    if custom_rules is not None:
        if not check_custom_rules(data, custom_rules):
            return False
    return True

def main():
    # Example usage
    file_path = 'path_to_your_data.csv'
    data = pd.read_csv(file_path)

    # Define expected data types
    expected_types = {
        'column1': 'int64',
        'column2': 'float64',
        'column3': 'object'
    }

    # Define custom validation rules
    custom_rules = {
        'column1': lambda x: (x > 0).all(),
        'column2': lambda x: (x >= 0).all()
    }

    # Validate the data
    is_valid = validate_data(data, expected_types, max_missing_ratio=0.1, custom_rules=custom_rules)
    if is_valid:
        print('Data validation passed')
    else:
        print('Data validation failed')

if __name__ == '__main__':
    main()
