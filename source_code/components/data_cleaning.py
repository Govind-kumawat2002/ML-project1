import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity,artifact_entity
class Datacleaning:
    def __init__(self,total_dataset_file_path:str,
                 total_train_file_path:str,
                  total_test_file_path:str,datacleaningconfig_obj:config_entity.Datacleaning):
            try:
                  
                  self.total_dataset_file_path=total_dataset_file_path
                  self.total_train_file_path = total_train_file_path
                  self.total_test_file_path= total_test_file_path
                  self.datacleaningconfig_obj=datacleaningconfig_obj
                  
            except Exception as e:
                  raise InsuranceException(e ,sys)
            
    def data_cleaning(self):
            
            try :
                  """
                  this funtion is used for data cleaning and manipulation of data"""
      
                  total_df=pd.read_csv(self.total_train_file_path)
                  total_df.drop_duplicates(inplace=True)
      
      
      
                  size_of_the_data = total_df.shape
                  logging.info(f'shape of the data {size_of_the_data}')  
      
      
      
                  # to handle the missing value
                  # logging.info('replacing na value with np.nan')
                  # total_df.replace(to_replace='na',value=np.NAN,inplace=True)
      
      
      
                  logging.info('replaced')    
                  # to handle the null value 
      
      
      
      
                  logging.info("remove the null  value from the dataset ")
                  total_df.dropna(inplace=True) 
                  # print(total_df)  
      
      
                  os.makedirs(self.datacleaningconfig_obj.clean_dataset_file_name,exist_ok = True)
                  clean_dataset_file_path=os.path.join(self.datacleaningconfig_obj.dataclean_dir,self.datacleaningconfig_obj.clean_dataset_file_name)
                  os.makedirs(self.datacleaningconfig_obj.clean_dataset_path,exist_ok = True)
                  total_train_file_path = os.path.join(self.datacleaningconfig_obj.clean_dataset_file_name,self.datacleaningconfig_obj.total_tarin_dataset_file_name)
      
      
                  total_test_file_path = os.path.join(self.datacleaningconfig_obj.clean_dataset_file_name,self.datacleaningconfig_obj.total_test_dataset_file_name)
      
                  total_df.to_csv(clean_dataset_file_path,index=False)
                  logging.info(f"successfully saved dataset data {clean_dataset_file_path}")
      
      
                  total_df.to_csv(total_train_file_path,index = False)
                  logging.info(f"successfully saved train data {total_train_file_path}")
      
                  total_df.to_csv(total_test_file_path,index = False)
                  logging.info(f"successfully saved test data {total_test_file_path}")


                  Dataclean_artfact=artifact_entity.Dataclean(clean_dataset_file_path,total_train_file_path,total_test_file_path)
                  return Dataclean_artfact



            except Exception as e :
                  raise InsuranceException(e, sys)
      
      


            



      
        