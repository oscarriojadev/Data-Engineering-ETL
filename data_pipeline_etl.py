# data_pipeline_etl.py

import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine
import os
import glob
import xml.etree.ElementTree as ET
import json

def extract_from_csv(file_path):
    """
    Extract data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Extracted data.
    """
    data = pd.read_csv(file_path)
    return data

def extract_from_excel(file_path):
    """
    Extract data from an Excel file.

    Parameters:
    file_path (str): Path to the Excel file.

    Returns:
    pd.DataFrame: Extracted data.
    """
    data = pd.read_excel(file_path)
    return data

def extract_from_json(file_path):
    """
    Extract data from a JSON file.

    Parameters:
    file_path (str): Path to the JSON file.

    Returns:
    pd.DataFrame: Extracted data.
    """
    with open(file_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)

def extract_from_xml(file_path):
    """
    Extract data from an XML file.

    Parameters:
    file_path (str): Path to the XML file.

    Returns:
    pd.DataFrame: Extracted data.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for child in root:
        row = {}
        for subchild in child:
            row[subchild.tag] = subchild.text
        data.append(row)
    return pd.DataFrame(data)

def extract_from_sql(query, connection_string):
    """
    Extract data from a SQL database.

    Parameters:
    query (str): SQL query to execute.
    connection_string (str): Connection string for the SQL database.

    Returns:
    pd.DataFrame: Extracted data.
    """
    engine = create_engine(connection_string)
    data = pd.read_sql(query, engine)
    return data

def transform_data(data, transformations):
    """
    Transform the data based on the specified transformations.

    Parameters:
    data (pd.DataFrame): Input data.
    transformations (dict): Dictionary of transformations to apply.

    Returns:
    pd.DataFrame: Transformed data.
    """
    for column, transformation in transformations.items():
        if transformation['type'] == 'fillna':
            data[column].fillna(transformation['value'], inplace=True)
        elif transformation['type'] == 'apply':
            data[column] = data[column].apply(transformation['function'])
        elif transformation['type'] == 'drop':
            data.drop(columns=[column], inplace=True)
    return data

def load_to_csv(data, file_path):
    """
    Load data to a CSV file.

    Parameters:
    data (pd.DataFrame): Data to load.
    file_path (str): Path to the CSV file.
    """
    data.to_csv(file_path, index=False)

def load_to_sql(data, table_name, connection_string, if_exists='replace'):
    """
    Load data to a SQL database.

    Parameters:
    data (pd.DataFrame): Data to load.
    table_name (str): Name of the table to load data into.
    connection_string (str): Connection string for the SQL database.
    if_exists (str): What to do if the table already exists ('replace', 'append', 'fail').
    """
    engine = create_engine(connection_string)
    data.to_sql(table_name, engine, if_exists=if_exists, index=False)

def main():
    # Example usage
    csv_file_path = 'path_to_your_csv_file.csv'
    excel_file_path = 'path_to_your_excel_file.xlsx'
    json_file_path = 'path_to_your_json_file.json'
    xml_file_path = 'path_to_your_xml_file.xml'
    sql_query = 'SELECT * FROM your_table'
    sql_connection_string = 'sqlite:///your_database.db'

    # Extract data from various sources
    csv_data = extract_from_csv(csv_file_path)
    excel_data = extract_from_excel(excel_file_path)
    json_data = extract_from_json(json_file_path)
    xml_data = extract_from_xml(xml_file_path)
    sql_data = extract_from_sql(sql_query, sql_connection_string)

    # Combine data from various sources
    combined_data = pd.concat([csv_data, excel_data, json_data, xml_data, sql_data], ignore_index=True)

    # Define transformations
    transformations = {
        'column1': {'type': 'fillna', 'value': 0},
        'column2': {'type': 'apply', 'function': lambda x: x * 2},
        'column3': {'type': 'drop'}
    }

    # Transform the data
    transformed_data = transform_data(combined_data, transformations)

    # Load the transformed data to a CSV file
    load_to_csv(transformed_data, 'transformed_data.csv')

    # Load the transformed data to a SQL database
    load_to_sql(transformed_data, 'transformed_data', sql_connection_string)

if __name__ == '__main__':
    main()
