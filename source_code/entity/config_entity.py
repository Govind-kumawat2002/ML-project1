# create the variable 
from source_code.logger import logging
from source_code.exception import InsuranceException
import os,sys
from datetime import datetime
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
        except Exception as e:
            
            raise InsuranceException(e,sys)
    
class Datavalidationconfig:
    def __init__(self,trainig_pipeline_config:TraningPipelineconfig):
        try:
            logging.info("intialiazing datavalidation  variable")
            self.datavalidation_dir = os.path.join(trainig_pipeline_config.artfact_dir,"data validation")
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

        except Exception as e:
            raise InsuranceException(e, sys)
       
class  DataTransFormationConfig:
    def __init__(self,traininng_pipeline_config_obj: TraningPipelineconfig):
        try:
            self.data_transormation_dir = os.path.join(traininng_pipeline_config_obj.artfact_dir,"Data Transormation") 
            self.transformed_data_file_path = os.path.join(self.data_transormation_dir,'transformed_data.csv')
            self.onehotedata_dir = os.path.join(self.data_transormation_dir,"onehot")
            self.standardized_dir = os.path.join(self.data_transormation_dir,"scaled")

            self.one_hot_data_file_path = os.path.join(self.onehotedata_dir,"one_hot_data.csv")
            self.onehote_encoder_model_path = os.path.join(self.onehotedata_dir,'onehot_encoder.lb')

            self.scaled_data_file_path = os.path.join(self.standardized_dir,"standard_data.csv")
            self.scaler_model_path  = os.path.join(self.standardized_dir,'robust_scaler.lb')

        except Exception as e:
            raise InsuranceException(e,sys)