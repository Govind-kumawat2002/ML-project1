from source_code.logger import logging
from source_code.exception import InsuranceException
import sys ,os 
from source_code.entity import config_entity ,artifact_entity
from source_code.dbconfig import connect_to_mogodb,connect_to_mysql
from source_code.utils import is_mongoconnected ,is_mysqlconnected
from source_code.components.data_ingestion import DataIngestion 
from source_code.components.data_cleaning import Datacleaning
from source_code.components.data_transformation import Datatransformation


# connect_to_mysql()

traning_pipeline_obj=config_entity.TraningPipelineconfig()

dataingestion_config_obj=config_entity.Datainegestincongif(trainig_pipeline_config=traning_pipeline_obj)

# mongo_connections=connect_to_mogodb(mogodb_string=dataingestion_config_obj.mongodb_string)
# is_mongoconnected(mongo_conne


# sql_connect=connect_to_mysql()
# is_mysqlconnected(mysql_connections=sql_connect)
# dataingestion_obj=DataIngestion(dataingestion_config_obj)
# dataingestion_obj.loading_dataset()




DataIngestion_obj=DataIngestion(dataingestion_config_obj)
loading_dataset_artifact_value=DataIngestion_obj.loading_dataset()

print(loading_dataset_artifact_value.Dataset_file_path)
print(loading_dataset_artifact_value.total_Test_file_path)
print(loading_dataset_artifact_value.total_Train_file_path)
# Datacleaning()
data_clean_pipeline=config_entity.Datacleaning(trainig_pipeline_config=traning_pipeline_obj)


object=Datacleaning(loading_dataset_artifact_value.Dataset_file_path,loading_dataset_artifact_value.total_Train_file_path,loading_dataset_artifact_value.total_Test_file_path,datacleaningconfig_obj=data_clean_pipeline)
object.data_cleaning()
# # object=Datacleaning(t)
print(object.total_dataset_file_path)




# data_tansfer_pipeline_obj=config_entity.DataTranformation(trainig_pipeline_config=traning_pipeline_obj)
# data_transfer_obj=Datatransformation(datatransfer_obj=data_tansfer_pipeline_obj)
# data_transfer_obj.datatransfer()



