from source_code.logger import logging
# from source_code.exception import InsuranceException
# from source_code.dbconfig import connect_to_mogodb
# from source_code.dbconfig import connect_to_mysql
import os 
import sys 
# hello=os.getenv('mogo_db_name')
# print(hello)
print(os.getenv('mogo_db_name'))
# class DataIngestion:
#     def __init__(self):
#         try:
#             pass
#         except Exception as e :
#             raise InsuranceException(e,sys)