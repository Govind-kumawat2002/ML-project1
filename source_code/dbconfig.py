import mysql.connector
from mysql.connector import Error
from source_code.logger import logging
from source_code.exception import InsuranceException
from dotenv import load_dotenv
import os,sys
import pandas as pd
from pymongo import MongoClient
load_dotenv()


def connect_to_mogodb(mogodb_string:str):
    try:
        client =MongoClient(mogodb_string)
        print("succesfully cooneted to mongodb")
        # mogo_database=client[mogo_db_name]
        # mogo_collection=mogo_database[mogo_collection_name]
        return client
    except Exception as e:
        custom_exception=InsuranceException(e,sys)
        print(f"unable to connect to the mogodb{ custom_exception.error_message}")
        logging.error(custom_exception.error_message)
        # print(f"Error connecting to MySQL: {e}")
        raise InsuranceException(e,sys)
        return None


def connect_to_mysql(host:str,user:str,password:str,database:str):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='13.53.42.161',       # Replace with your host, e.g., '127.0.0.1'
            user='Admin',            # Replace with your MySQL username
            password='password123!',        # Replace with your MySQL password
            database='room', # Replace with your database name
            allow_local_infile=True  # Enable loading local files
        )
        logging.info("connecting to with database..")
        
        if connection.is_connected():
            print("Connected to MySQL Server")
            logging.info("successfully connected with database..")
            return connection
    except Error as e:
        custom_exception=InsuranceException(e,sys)
        custom_exception.error_message
        logging.error(custom_exception.error_message)
        # print(f"Error connecting to MySQL: {e}")
        raise InsuranceException(e,sys)
        return None
    







# def create_table(connection):
#     try:
#         cursor = connection.cursor()
#         # Define the table structure
#         create_table_query = """
#         CREATE TABLE IF NOT EXISTS insurance_data (
#             bmi FLOAT NOT NULL,
#             children INT NOT NULL,
#             smoker VARCHAR(10) NOT NULL,
#             region VARCHAR(50) NOT NULL,
#             charges FLOAT NOT NULL
#         );
#         """
#         cursor.execute(create_table_query)
#         print("Table 'insurance_data' created successfully (or already exists).")
#     except Error as e:
#         custom_exception=InsuranceException(e,sys)
#         custom_exception.error_message
#         logging.error(custom_exception.error_message)
#         # print(f"Error creating table: {e}")
#         raise InsuranceException(e,sys)

# def dump_data_sql(connection, csv_file_path):
#     try:
#         cursor = connection.cursor()
#         # Use the LOCAL option to load from a local file
#         load_data_query = f"""
#         LOAD DATA LOCAL INFILE '{csv_file_path}'
#         INTO TABLE insurance_data
#         FIELDS TERMINATED BY ','   -- Column separator
#         ENCLOSED BY '"'            -- Text delimiter (optional)
#         LINES TERMINATED BY '\\n'  -- Row delimiter
#         IGNORE 1 LINES;           -- Ignore header row
#         """
#         cursor.execute(load_data_query)
#         connection.commit()  # Commit the changes to the database
#         print("Data loaded successfully from CSV.")
#     except Error as e:
#         # print(f"Error loading data from CSV: {e}")
#         custom_exception=InsuranceException(e,sys)
#         custom_exception.error_message
#         logging.error(custom_exception.error_message)

# # Connect to MySQL
# connection = connect_to_mysql()
# if connection:
#     # Create the table if it doesn't exist
#     create_table(connection)
    
#     # Specify the path to your CSV file
#     csv_file_path = './firsthalf_data.csv'  # Update this path
    
#     # Load data from CSV into the table
#     dump_data_sql(connection, csv_file_path)

#     # Close connection
#     connection.close()
#     print("Connection closed.")
