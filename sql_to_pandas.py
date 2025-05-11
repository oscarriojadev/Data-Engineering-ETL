# sql_to_pandas.py

import pandas as pd
import sqlite3
import psycopg2
import pymysql
from sqlalchemy import create_engine

def connect_to_sqlite(database_path):
    """
    Connect to a SQLite database.

    Parameters:
    database_path (str): Path to the SQLite database file.

    Returns:
    sqlite3.Connection: SQLite database connection.
    """
    connection = sqlite3.connect(database_path)
    return connection

def connect_to_postgresql(host, database, user, password, port=5432):
    """
    Connect to a PostgreSQL database.

    Parameters:
    host (str): Database host.
    database (str): Database name.
    user (str): Database user.
    password (str): Database password.
    port (int): Database port.

    Returns:
    psycopg2.extensions.connection: PostgreSQL database connection.
    """
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    return connection

def connect_to_mysql(host, database, user, password, port=3306):
    """
    Connect to a MySQL database.

    Parameters:
    host (str): Database host.
    database (str): Database name.
    user (str): Database user.
    password (str): Database password.
    port (int): Database port.

    Returns:
    pymysql.connections.Connection: MySQL database connection.
    """
    connection = pymysql.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    return connection

def execute_query(connection, query):
    """
    Execute a SQL query and return the results as a Pandas DataFrame.

    Parameters:
    connection: Database connection.
    query (str): SQL query to execute.

    Returns:
    pd.DataFrame: Query results.
    """
    return pd.read_sql(query, connection)

def close_connection(connection):
    """
    Close a database connection.

    Parameters:
    connection: Database connection.
    """
    connection.close()

def main():
    # Example usage for SQLite
    sqlite_database_path = 'path_to_your_sqlite_database.db'
    sqlite_connection = connect_to_sqlite(sqlite_database_path)
    sqlite_query = 'SELECT * FROM your_table'
    sqlite_data = execute_query(sqlite_connection, sqlite_query)
    print('SQLite Data:')
    print(sqlite_data.head())
    close_connection(sqlite_connection)

    # Example usage for PostgreSQL
    postgresql_host = 'your_postgresql_host'
    postgresql_database = 'your_postgresql_database'
    postgresql_user = 'your_postgresql_user'
    postgresql_password = 'your_postgresql_password'
    postgresql_port = 5432
    postgresql_connection = connect_to_postgresql(postgresql_host, postgresql_database, postgresql_user, postgresql_password, postgresql_port)
    postgresql_query = 'SELECT * FROM your_table'
    postgresql_data = execute_query(postgresql_connection, postgresql_query)
    print('PostgreSQL Data:')
    print(postgresql_data.head())
    close_connection(postgresql_connection)

    # Example usage for MySQL
    mysql_host = 'your_mysql_host'
    mysql_database = 'your_mysql_database'
    mysql_user = 'your_mysql_user'
    mysql_password = 'your_mysql_password'
    mysql_port = 3306
    mysql_connection = connect_to_mysql(mysql_host, mysql_database, mysql_user, mysql_password, mysql_port)
    mysql_query = 'SELECT * FROM your_table'
    mysql_data = execute_query(mysql_connection, mysql_query)
    print('MySQL Data:')
    print(mysql_data.head())
    close_connection(mysql_connection)

if __name__ == '__main__':
    main()
