# # import sys
# # try:
# #     10/0

# # except Exception as e:
# #     rror_class,error_message,exe_tb=sys.exc_info()
# #     print(rror_class,error_message,exe_tb)
# #     print(exe_tb.tb_frame.f_lineno)
# #     print(exe_tb.tb_frame.f_code.co_filename)
    

# # import mysql.connector # type: ignore

# # # Connect to the database
# # conn = mysql.connector.connect(
# #     host="13.51.166.182",
# #     user="root",
# #     password="1234",
# #     database="jai"

# # )
# # if conn.is_connected():
# #     print("hm connect ho chuke ")
# # else:
# #     print("not conn")  
# # import mysql.connector

# # # Establish the connection
# # # try:
# # conn = mysql.connector.connect(
# #       host="13.60.56.130 ",
# #         user="root",
# #         password="1234",
# #         database="jai"
# #     )
# # if conn.is_connected():
# #         print("Connected to MySQL")
# # else:
# #         print("sql is not connected ")
# import mysql.connector
# from mysql.connector import Error

# def connect_to_mysql():
#     try:
#         # Connect to the MySQL server
#         connection = mysql.connector.connect(
#             host='localhost',       # Replace with your host, e.g., '127.0.0.1'
#             user='root',            # Replace with your MySQL username
#             password='1234',        # Replace with your MySQL password
#             database='mlproject_db', # Replace with your database name
#             allow_local_infile=True  # Enable loading local files
#         )
        
#         if connection.is_connected():
#             print("Connected to MySQL Server")
#             return connection
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
#         return None

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
#         print(f"Error creating table: {e}")

# def load_data_from_csv(connection, csv_file_path):
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
#         print(f"Error loading data from CSV: {e}")

# # Connect to MySQL
# connection = connect_to_mysql()
# if connection:
#     # Create the table if it doesn't exist
#     create_table(connection)
    
#     # Specify the path to your CSV file
#     csv_file_path = './firsthalf_data.csv'  # Update this path
    
#     # Load data from CSV into the table
#     load_data_from_csv(connection, csv_file_path)

#     # Close connection
#     connection.close()
#     print("Connection closed.")


# from source_code.dbconfig import connect_to_mogodb,connect_to_mysql


# sql_connection=connect_to_mysql(host='16.171.3.98',user="Admin",password='Pass@12345',database='room')

# if sql_connection.is_connected():
#     print("connected")
# else:
#     print("not connected")


# cursor =sql_connection.cursor()
# cursor.execute("SELECT * FROM insurance_data")
# rows=cursor.fetchall()
# for x in rows:
#     print(x)


# import mysql.connector
# connection =mysql.connector.connect( host="51.20.191.241",
#             user="Admin",
#             password="Pass@12345",
#             database="room")
# if connection.is_connected():
#     print("connection")
# else:
#     print("not connected")


# logging.info("connect with mysql ")

# cursor =sql_connection.cursor()
# cursor.execute("SELECT * FROM insurance_data")
# rows = cursor.fetchall()
# for row in rows:
#         print(row)



# import pandas as pd
# import mysql.connector
# from mysql.connector import Error

# # Function to insert CSV data into MySQL
# def insert_csv_to_mysql(csv_file, host, user, password, database, table_name):
#     try:
#         # Read CSV data into a Pandas DataFrame
#         df = pd.read_csv(csv_file)

#         # Connect to the MySQL database
#         connection = mysql.connector.connect(
#           host="51.20.191.241 ",
# user="root",
# password="Password123!",
# database="room"
#                     )
        

#         if connection.is_connected():
#             print(f"Connected to MySQL database {database}")

#             # Create a cursor object
#             cursor = connection.cursor()

#             # Iterate over the DataFrame and insert data into MySQL
#             for index, row in df.iterrows():
#                 # Create an INSERT query
#                 insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
                
#                 # Insert the row data into the table
#                 cursor.execute(insert_query, tuple(row))
                
#             # Commit the transaction
#             connection.commit()
#             print(f"Successfully inserted {len(df)} rows into {table_name}.")

#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         # Close the cursor and connection
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed.")

# # Define your CSV file and MySQL details
# csv_file = 'E:\ML-project1\split_part_1.csv'  # Path to your CSV file
# host="51.20.191.241 ",
# user="root",
# password="Password123!",
# database="room"
# table_name = 'insurance_data'


# # Call the function to insert CSV data to MySQL
# insert_csv_to_mysql(csv_file=csv_file, host=host, user=user, password=password, database=database, table_name=table_name)



import pandas as pd
import mysql.connector
from mysql.connector import Error

# Function to insert CSV data into MySQL
def insert_csv_to_mysql(csv_file, host, user, password, database, table_name):
    try:
        # Read CSV data into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print(f"Connected to MySQL database {database}")

            # Create a cursor object
            cursor = connection.cursor()

            # Iterate over the DataFrame and insert data into MySQL
            for index, row in df.iterrows():
                # Replace NaN values with None for MySQL NULL handling
                row = tuple(None if pd.isna(x) else x for x in row)

                # Create an INSERT query
                insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
                
                # Insert the row data into the table
                cursor.execute(insert_query, row)
                
            # Commit the transaction
            connection.commit()
            print(f"Successfully inserted {len(df)} rows into {table_name}.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Define your CSV file and MySQL details
csv_file = r"E:\ML-project1\split_part_1.csv"  # Use raw string or double backslashes
host = "51.20.191.241"  # Removed extra space
user = "Admin"
password = "Pass@12345"
database = "room"
table_name = "insurance_data_sql"

# Call the function to insert CSV data to MySQL
insert_csv_to_mysql(csv_file=csv_file, host=host, user=user, password=password, database=database, table_name=table_name)
