# create the variable 
from source_code.logger import logging
from source_code.exception import InsuranceException
import os,sys
from datetime import datetime






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
            self.mysql_user = os.getenv('mysql_user')
            self.mysql_password = os.getenv('mysql_user_pass')
            self.mysql_database= os.getenv('mysql_database')
            self.mongodb_string=os.getenv("mogodb_string")
            self.mongo_db_name=os.getenv('mogo_db_name')
            self.mongo_collection_name=os.getenv('mogo_collection_name')


            
            

        except Exception as e:
            
            raise InsuranceException(e,sys)
        