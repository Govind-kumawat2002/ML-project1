import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity,artifact_entity
class Datacleaning:
    def __init__(self):
        try:
            dataset_file_path=artifact_entity.Dataingenstionartifact.Dataset_file_path ,
            train_file_path=artifact_entity.Dataingenstionartifact.Train_file_path,
            test_file_path=artifact_entity.Dataingenstionartifact.Test_file_path
            total_df=pd.read_csv(dataset_file_path)
            total_df.drop_duplicates(inplace=True)
            size_of_the_data = total_df.shape
            logging.info(f'shape of the data {size_of_the_data}')

            # to handle the missing value
            logging.info('replacing na value with np.nan')
            total_df.replace(to_replace='na',value=np.NAN,inplace=True)
            logging.info('replaced')

            # to handle the null value 
            logging.info("remove the null  value from the dataset ")
            total_df.dropna(inplace=True)

            



            pass
        except Exception as e:
            raise  InsuranceException(e,sys)
        