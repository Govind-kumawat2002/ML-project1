from source_code.logger import logging
from source_code.exception import InsuranceException
import sys ,os 
from source_code.entity import config_entity ,artifact_entity
from source_code.dbconfig import connect_to_mogodb,connect_to_mysql
from source_code.utils import is_mongoconnected ,is_mysqlconnected
from source_code.components.data_ingestion import DataIngestion 
from source_code.components.data_cleaning import Datacleaning
# from source_code.components.data_transformation import Datatransformation
from source_code.components.data_validation import Datatvalidation
from source_code.components.data_transformation import DataTransformation
import pandas as pd 


# connect_to_mysql()
# connect_to_mogodb()

traning_pipeline_obj=config_entity.TraningPipelineconfig()

dataingestion_config_obj=config_entity.Datainegestincongif(trainig_pipeline_config=traning_pipeline_obj)


dataingestion_obj=DataIngestion(dataingestion_config_obj)
dataingestionArtifact_obj =  dataingestion_obj.loading_dataset()


data_validation_config=config_entity.Datavalidationconfig(trainig_pipeline_config=traning_pipeline_obj)


datavalidation_object=Datatvalidation(datavalidation_obj=data_validation_config,data_ingestion_artificat=dataingestionArtifact_obj)
data_validation_artifact=datavalidation_object.checkthedata_valid()
# print(data_validation_artifact)

data_cleaning_config=config_entity.Datacleaningconfig(trainig_pipeline_config=traning_pipeline_obj)
data_cleaning_obj=Datacleaning(data_cleaning_artifact=data_validation_artifact,data_cleaning_config=data_cleaning_config)
data_cleaning_obj_path=data_cleaning_obj.clean_data()


data_transformation_config_obj =  config_entity.DataTransFormationConfig(traininng_pipeline_config_obj=traning_pipeline_obj)
data_transormation_obj =  DataTransformation(
                    data_transformation_config=data_transformation_config_obj,
                    data_cleaning_artifact=data_cleaning_obj_path
)
data_transormation_artifact =  data_transormation_obj.transform_initiate()
print("Data transformation Done ✅")


# data_transfromation_obj=DataTransformation(datatransformation_artifact=data_cleaning_obj_path)
# data_transfromation_obj.transform_data()

# data_transfromation_obj.handle_missing_values()



















# # Datacleaning()
# data_cleaning_config=config_entity.Datacleaningconfig(trainig_pipeline_config=traning_pipeline_obj)
# # print(data_cleaning_config.clean_dataset_file_name)
# data_validation_artifact=artifact_entity.DatavalidationArtifact(valid_Dataset_file_path=d)
# print(data_validation_artifact.valid_Dataset_file_path)



# print(artifact_entity.DatavalidationArtifact.valid_Dataset_file_path)









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



