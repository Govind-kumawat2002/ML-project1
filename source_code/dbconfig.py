import mysql.connector
from mysql.connector import Error
from source_code.logger import logging
from source_code.exception import InsuranceException
from dotenv import load_dotenv
import os,sys
import pandas as pd
from pymongo import MongoClient
load_dotenv()
# load_dotenv()
host_name=os.getenv('mysql_host')
mysql_user=os.getenv('mysql_user')
mysql_user_password=os.getenv('mysql_user_password')
mysql_database=os.getenv('mysql_database')

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


def connect_to_mysql():
    try:
        # Connect to the MySQL server

        
        connection = mysql.connector.connect(
            host=host_name,       # Replace with your host, e.g., '127.0.0.1'
            user=mysql_user,            # Replace with your MySQL username
            password=mysql_user_password,        # Replace with your MySQL password
            database=mysql_database, # Replace with your database name
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
    







