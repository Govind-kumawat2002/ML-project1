from source_code.logger import logging
from source_code.exception import InsuranceException
import sys ,os 
from source_code.entity import config_entity
from source_code.dbconfig import connect_to_mogodb
from source_code.utils import is_mongoconnected
from source_code.components.data_ingestion import DataIngestion

traning_pipeline_obj=config_entity.TraningPipelineconfig()

dataingestion_config_obj=config_entity.Datainegestincongif(trainig_pipeline_config=traning_pipeline_obj)

mongo_connections=connect_to_mogodb(mogodb_string=dataingestion_config_obj.mongodb_string)
is_mongoconnected(mongo_connections)
obj=DataIngestion(dataingestion_config_obj)
obj.loading_dataset()

