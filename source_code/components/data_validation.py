import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity,artifact_entity


class Datatvalidation:
    def __init__(self,datavalidation_obj:config_entity.Datavalidationconfig,data_ingestion_artificat:artifact_entity.Dataingenstionartifact):
        try:
            self.datavalidation_obj=datavalidation_obj
            self.data_ingestion_artificat_obj=data_ingestion_artificat
        except Exception as e:
             raise InsuranceException(e ,sys)

    def load_dataset_validation(self):
            try:
                
                df=pd.read_csv(self.data_ingestion_artificat_obj.dataset_file_path)
                print(df.shape)

                
    
        # Define validation functions
                @staticmethod
                def validate_sex(value):
                    return value in ["male", "female"]
                
                @staticmethod
                def validate_bmi(value):
                    return isinstance(value, (int, float)) and value > 0
                
                @staticmethod
                def validate_children(value):
                    return isinstance(value, int) and value >= 0
                
                @staticmethod
                def validate_smoker(value):
                    return value in ["yes", "no"]
                
                @staticmethod
                def validate_region(value):
                    return value in ["southeast", "southwest", "northeast", "northwest"]
                
                @staticmethod
                def validate_charges(value):
                    return isinstance(value, (int, float)) and value >= 0

                # Apply validation checks
                invalid_rows = df[
                    (~df["sex"].apply(validate_sex)) |
                    (~df["bmi"].apply(validate_bmi)) |
                    (~df["children"].apply(validate_children)) |
                    (~df["smoker"].apply(validate_smoker)) |
                    (~df["region"].apply(validate_region)) |
                    (~df["charges"].apply(validate_charges))
                ]

                # Display validation results
                if invalid_rows.empty:
                    # print(invalid_rows)
                    print("✅ Data is valid!")
                    # print(type(invalid_rows))
                    os.makedirs(self.datavalidation_obj.datavalidation_dir,exist_ok = True)


                    valid_file_path=os.path.join(self.datavalidation_obj.datavalidation_dir,self.datavalidation_obj.valid_data_file_name)
                    df.to_csv(valid_file_path,index=False)
                    logging.info(f"successfully saved dataset data {valid_file_path}")
                else:
                    print("⚠️ Invalid data found:")
                    invalid_file_path=os.path.join(self.datavalidation_obj.datavalidation_dir,self.datavalidation_obj.invalid_data_file_name)
                    df.to_csv(invalid_file_path,index=False)
                    logging.info(f"successfully saved dataset data {invalid_file_path}")
                    # print(invalid_rows)
                    df.drop(invalid_rows.index,inplace=True)
            except Exception as e:
                 raise InsuranceException(e ,sys)


            
            
