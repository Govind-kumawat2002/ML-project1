import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity, artifact_entity

class Datacleaning:
    def __init__(self, data_cleaning_artifact: artifact_entity.DatavalidationArtifact,
                 data_cleaning_config: config_entity.Datacleaningconfig):
        try:
            self.data_cleaning_config = data_cleaning_config
            self.data_cleaning_artifact = data_cleaning_artifact
            self.dataset = pd.read_csv(data_cleaning_artifact.valid_Dataset_file_path)
            # print(self.dataset)
        except Exception as e:
            raise InsuranceException(e, sys)

    def clean_data(self):
        try:
            df = self.dataset.copy()

            """
            Cleans a pandas DataFrame by:
            - Removing duplicate rows
            - Filling missing values with column mean (for numerical columns)
            - Stripping whitespace from string columns
            - Dropping columns with more than 50% missing values
            
            Returns:
            pd.DataFrame: The cleaned DataFrame
            """
            
            # Remove duplicates
            df = df.drop_duplicates()
            
            # Drop columns with more than 50% missing values
            threshold = len(df) * 0.5
            df = df.dropna(thresh=threshold, axis=1)
            
            # Fill missing values with column mean for numerical columns
            num_cols = df.select_dtypes(include=['number']).columns
            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
            
            # Strip whitespace from string columns
            str_cols = df.select_dtypes(include=['object']).columns
            df[str_cols] = df[str_cols].apply(lambda x: x.str.strip() if x.dtype == "object" else x)


            os.makedirs(self.data_cleaning_config.dataclean_dir,exist_ok=True)
            clean_file_path=os.path.join(self.data_cleaning_config.dataclean_dir,self.data_cleaning_config.clean_dataset_file_name)
            # os.makedirs(self.data_cleaning_config.dataclean_dir, exist_ok=True)
            # clean_file_path = os.path.join(self.data_cleaning_config.dataclean_dir, self.data_cleaning_config.clean_dataset_file_name)
            df.to_csv(clean_file_path, index=False)

            logging.info(f"Successfully saved clean dataset at {clean_file_path}")
            datacleaning_artifact=artifact_entity.DatacleaningArtifact(clean_file_path=clean_file_path)
      
            return datacleaning_artifact
        except Exception as e:
            raise InsuranceException(e, sys)