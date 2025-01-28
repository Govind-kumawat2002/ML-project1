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
import pandas as pd 
import numpy as np 
# import entity
from source_code.entity import config_entity,artifact_entity
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self,dataingestionconfig_obj:config_entity.Datainegestincongif):
        try:
            self.dataingestionconfig_obj=dataingestionconfig_obj
        except Exception as e :
            raise InsuranceException(e,sys)
        
    ## loading the dataset 
    def loading_dataset(self):

        """this function is used to load the dataset from the database, like (mysql ,mongodb). and saved the data in local dir 
        """
        try:
            mongoconnection =connect_to_mogodb(mogodb_string=self.dataingestionconfig_obj.mongodb_string)
            logging.info("connected with mongo db")
            mongodb_database =mongoconnection[self.dataingestionconfig_obj.mongo_db_name]
        
            mongo_connection_nane =mongodb_database[self.dataingestionconfig_obj.mongo_collection_name]
            mongo_documents = mongo_connection_nane.find()
            logging.info("succssfully loaded data from mongodb atlas")
            documents=pd.DataFrame(list(mongo_documents))
            logging.info("succssfully drop the _id coloum form dataset ")
            documents.drop('_id',axis=1,inplace=True)


            infomation_of_data=documents.info()
            logging.info(f"infomation of dataset {infomation_of_data}")


            shape_of_data=documents.shape
            logging.info(f"shape of the data{shape_of_data}")
            logging.info('replacing na value with np.nan')


            # documents.replace(to_replace='na',value=np.NAN,inplace=True)
            # logging.info('replaced')
            # # to save the entire data at one place, "feature_store"
            # logging.info('Saving the entire data into the feature store.')
            # feature_store = os.path.dirname(self.data_ingestion_dir.feature_store_file_path)
            # os.makedirs(feature_store,exist_ok=True) # directory path
            # documents.to_csv(path_or_buf=self.data_ingestion_dir.feature_store_file_path,index=False,header=True)
            # to split the data

            logging.info('spliting the data into train and test data')
            train_df,test_df = train_test_split(documents,test_size=self.dataingestionconfig_obj.test_size,random_state=42)

            # to store training data & testing data
            logging.info('storing the training and test file.')
            # training_data_file_path = os.path.dirname(self.dataingestionconfig_obj.dataingestion_dir)
            os.makedirs(self.dataingestionconfig_obj.dataingestion_dir, exist_ok=True) 
            # os.join.path(self.dataingestionconfig_obj.dataingestion_dir)
            os.makedirs(self.dataingestionconfig_obj.dataset_path,exist_ok = True)
            dataset_file_path=os.path.join(self.dataingestionconfig_obj.dataingestion_dir,self.dataingestionconfig_obj.dataset_file_name)
            

            os.makedirs(self.dataingestionconfig_obj.dataset_path,exist_ok = True)
            # dataset_path =
            train_file_path = os.path.join(self.dataingestionconfig_obj.dataset_path,self.dataingestionconfig_obj.train_dataset_file_name)
            test_file_path = os.path.join(self.dataingestionconfig_obj.dataset_path,self.dataingestionconfig_obj.test_dataset_file_name)

            documents.to_csv(dataset_file_path,index=False)
            logging.info(f"successfully saved dataset data {dataset_file_path}")


            train_df.to_csv(train_file_path,index = False)
            logging.info(f"successfully saved train data {train_file_path}")

            test_df.to_csv(test_file_path,index = False)
            logging.info(f"successfully saved test data {test_file_path}")





            DataIngestion_artfact=artifact_entity.Dataingenstionartifact(dataset_file_path,train_file_path,test_file_path)
            return DataIngestion_artfact

 
        except Exception as e:
            raise InsuranceException(e,sys)