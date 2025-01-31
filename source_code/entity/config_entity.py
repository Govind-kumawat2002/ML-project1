# create the variable 
from source_code.logger import logging
from source_code.exception import InsuranceException
import os,sys
from datetime import datetime
# from source_code.entity import artifact_entity,config_entity
# from artifact_entity import Dataingenstionartifact
import pandas as pd 
# import artifact_entity
# from source_code.entity.artifact_entity im





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

            self.host = os.getenv('mysql_host')
            self.mysql_user = os.getenv('mysql_user')
            self.mysql_password = os.getenv('mysql_user_password')
            self.mysql_database= os.getenv('mysql_database')





            self.mongodb_string=os.getenv("mogodb_string")
            self.mongo_db_name=os.getenv('mogo_db_name')
            self.mongo_collection_name=os.getenv('mogo_collection_name')
            self.test_size = 0.2
            self.dataset_file_name = "insurance.csv"
            self.train_dataset_file_name="train.csv"
            self.test_dataset_file_name = "test.csv"
            # self.mysql_train_dataset_file_name = 'train.csv'
            # self.mysql_test_dataset_file_name= 'test.csv'

            # self.total_tarin_dataset_file_name = self.mysql_train_dataset_file_name+self.mongo_train_dataset_file_name
            # self.total_test_dataset_file_name = self.mongo_test_dataset_file_name+self.mysql_test_dataset_file_name

            # self.mysql_database = os.getenv('mysql_database')
            # self.mysql_password = 


            
            

        except Exception as e:
            
            raise InsuranceException(e,sys)
        



        

        
class Datavalidationconfig:
    def __init__(self,trainig_pipeline_config:TraningPipelineconfig):
        try:
            logging.info("intialiazing datavalidation  variable")
            self.datavalidation_dir = os.path.join(trainig_pipeline_config.artfact_dir,"data validation")
            # self.valid_data_validation_dir = os.path.join(self.datavalidation_dir,"valid validation data")
            # self.invalid_data_validation_dir=os.path.join(self.datavalidation_dir,"invalid validation data")
            self.valid_data_file_name = "valid_Data.csv"
            self.invalid_data_file_name = "invalid_Data.csv"

             
        except Exception as e :
            raise InsuranceException(e ,sys)
        









        
class Datacleaningconfig:
    def __init__(self,trainig_pipeline_config:TraningPipelineconfig):

        try:
            logging.info("intialiazing datacleaning  variable")

            self.dataclean_dir = os.path.join(trainig_pipeline_config.artfact_dir,"data cleaning")
            self.clean_dataset_file_name = "clean_insurance.csv"
            self.clean_dataset_path= os.path.join(self.dataclean_dir,"Clean Dataset")



            self.mongo_train_dataset_file_name="train.csv"
            self.mongo_test_dataset_file_name = "test.csv"
            self.mysql_train_dataset_file_name = 'train.csv'
            self.mysql_test_dataset_file_name= 'test.csv'

            # self.total_tarin_dataset_file_name = self.mysql_train_dataset_file_name+self.mongo_train_dataset_file_name
            # self.total_test_dataset_file_name = self.mongo_test_dataset_file_name+self.mysql_test_dataset_file_name


        except Exception as e:
            raise InsuranceException(e, sys)
        
class DataTranformationconfig:
    def __init__(self,trainig_pipeline_config:TraningPipelineconfig):
        try:
            logging.info("intialiazing datatranforamtion  variable")
            self.cleaning_dataset = Dataclean.clean_dataset_file_path

            pass
        except Exception as e:
            raise InsuranceException(e , sys)
