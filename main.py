from source_code.logger import logging
from source_code.exception import InsuranceException
import sys ,os 
from source_code.entity import config_entity ,artifact_entity
from source_code.dbconfig import connect_to_mogodb,connect_to_mysql
from source_code.utils import is_mongoconnected ,is_mysqlconnected
from source_code.components.data_ingestion import DataIngestion 
# from source_code.components.data_cleaning import Datacleaning
# from source_code.components.data_transformation import Datatransformation
from source_code.components.data_validation import Datatvalidation
import pandas as pd 


# connect_to_mysql()
# connect_to_mogodb()

traning_pipeline_obj=config_entity.TraningPipelineconfig()

dataingestion_config_obj=config_entity.Datainegestincongif(trainig_pipeline_config=traning_pipeline_obj)


dataingestion_obj=DataIngestion(dataingestion_config_obj)
dataingestionArtifact_obj =  dataingestion_obj.loading_dataset()


data_validation_config=config_entity.Datavalidationconfig(trainig_pipeline_config=traning_pipeline_obj)
datavalidation_object=Datatvalidation(datavalidation_obj=data_validation_config,data_ingestion_artificat=dataingestionArtifact_obj)

# print(datavalidation_object.data_ingestion_artificat_obj.dataset_file_path)
datavalidation_object.load_dataset_validation()













# Datatvalidation(data_ingestion_artificat=loading_dataset_artifact_value,
#                 )
# print(loading_dataset_artifact_value.Dataset_file_path)
# print(loading_dataset_artifact_value.total_Test_file_path)
# print(loading_dataset_artifact_value.total_Train_file_path)









# Datacleaning()
# data_clean_pipeline=config_entity.Datacleaning(trainig_pipeline_config=traning_pipeline_obj)


# object=Datacleaning(loading_dataset_artifact_value.Dataset_file_path,loading_dataset_artifact_value.total_Train_file_path,loading_dataset_artifact_value.total_Test_file_path,datacleaningconfig_obj=data_clean_pipeline)
# object.data_cleaning()
# # # object=Datacleaning(t)
# print(object.total_dataset_file_path)




# data_tansfer_pipeline_obj=config_entity.DataTranformation(trainig_pipeline_config=traning_pipeline_obj)
# data_transfer_obj=Datatransformation(datatransfer_obj=data_tansfer_pipeline_obj)
# data_transfer_obj.datatransfer()



