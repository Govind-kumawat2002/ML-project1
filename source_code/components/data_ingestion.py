import os 
import numpy
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
from source_code.dbconfig import connect_to_mogodb
from source_code.dbconfig import connect_to_mysql
# from source_code.entity import
import os 
import sys 
import pymongo
# import entity
from source_code.entity import config_entity,artifact_entity


class DataIngestion:
    def __init__(self,dataingestionconfig_obj:config_entity.Datainegestincongif):
        try:
            self.dataingestionconfig_obj=dataingestionconfig_obj
        except Exception as e :
            raise InsuranceException(e,sys)
        
    ## loading the dataset 
    def loading_dataset(self):

        """this function is used to load the dataset from the database, like (mysql ,mongodb).
        """
        try:
            mongoconnection =connect_to_mogodb(mogodb_string=self.dataingestionconfig_obj.mongodb_string)
            logging.info("connected with mongo db")
            # mysqlconnection=connect_to_mysql(database=self.dataingestionconfig_obj.mysql_database,
            #                                  user=self.dataingestionconfig_obj.mysql_user,
            #                                  password=self.dataingestionconfig_obj.mysql_password)
            mongodb_database =mongoconnection[self.dataingestionconfig_obj.mongo_db_name]
        
            mongo_connection_nane =mongodb_database[self.dataingestionconfig_obj.mongo_collection_name]
            mongo_documents = mongo_connection_nane.find()
            logging.info("succssfully loaded data from mongodb atlas")
            
        except Exception as e:
            raise InsuranceException(e,sys)