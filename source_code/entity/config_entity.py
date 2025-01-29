# create the variable 
from source_code.logger import logging
from source_code.exception import InsuranceException
import os,sys
from datetime import datetime
# from source_code.entity import artifact_entity,config_entity
from artifact_entity import Dataingenstionartifact
import pandas as pd 






class TraningPipelineconfig:
    def __init__(self):
        
        try:
            logging.info("Initializing artifact directory ")
            self.artfact_dir = os.path.join(os.getcwd(),"Artifacts",datetime.now().strftime("%d-%m-%y-%H-%M-%S"))
        except Exception as e :
            obj=InsuranceException(e,sys)
            logging.info(obj.error_message)
            raise InsuranceException(e,sys)
        
class Datainegestincongif:
    def __init__(self,trainig_pipeline_config:TraningPipelineconfig):
        try:
            logging.info("intialiazing dataingestionconfig variable")
            self.dataingestion_dir = os.path.join(trainig_pipeline_config.artfact_dir,"data ingestion")
            self.dataset_path= os.path.join(self.dataingestion_dir,"Dataset")
            self.train_file_path = os.path.join(self.dataingestion_dir,"train_file_path")
            self.mysql_user = os.getenv('mysql_user')
            self.mysql_password = os.getenv('mysql_user_pass')
            self.mysql_database= os.getenv('mysql_database')
            self.mongodb_string=os.getenv("mogodb_string")
            self.mongo_db_name=os.getenv('mogo_db_name')
            self.mongo_collection_name=os.getenv('mogo_collection_name')
            self.test_size = 0.2
            self.dataset_file_name = "insurance.csv"
            self.train_dataset_file_name="train.csv"
            self.test_dataset_file_name = "test.csv"


            
            

        except Exception as e:
            
            raise InsuranceException(e,sys)
        
class Datacleaning:
    def __init__(self,Dataingenstionartifact:Dataingenstionartifact):
        try:
            self.total_df=pd.read_csv('E:\ML-project1\Artifacts\28-01-25-11-58-28\data ingestion\insurance.csv')
            
            # logging.info("intialiazing datacleaning  variable")

            # self.dataset_file_path =Dataingenstionartifact.Dataset_file_path
            # self.train_file_path = Dataingenstionartifact.Train_file_path
            # self.test_file_path = Dataingenstionartifact.Test_file_path
        except Exception as e:
            raise InsuranceException(e, sys)
        