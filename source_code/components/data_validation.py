# import os 
# import numpy as np 
# import sys
# import pandas as pd 
# from source_code.logger import logging
# from source_code.exception import InsuranceException
# # load dataset from dir 
# from source_code.entity import config_entity,artifact_entity


# class Datatvalidation:
#     def __init__(self,datavalidation_obj:config_entity.Datavalidationconfig,data_ingestion_artificat:artifact_entity.Dataingenstionartifact):
#         try:
#             self.datavalidation_obj=datavalidation_obj
#             self.data_ingestion_artificat_obj=data_ingestion_artificat
#         except Exception as e:
#              raise InsuranceException(e ,sys)

#     def load_dataset_validation(self):
           
                
#                 df=pd.read_csv(self.data_ingestion_artificat_obj.dataset_file_path)
#                 # print(df.shape)

                
    
#         # Define validation functions
#                 @staticmethod
#                 def validate_sex(value):
#                     return value in ["male", "female"]
                
#                 @staticmethod
#                 def validate_bmi(value):
#                     return isinstance(value, (int, float)) and value > 0
                
#                 @staticmethod
#                 def validate_children(value):
#                     return isinstance(value, int) and value >= 0
                
#                 @staticmethod
#                 def validate_smoker(value):
#                     return value in ["yes", "no"]
                
#                 @staticmethod
#                 def validate_region(value):
#                     return value in ["southeast", "southwest", "northeast", "northwest"]
                
#                 @staticmethod
#                 def validate_charges(value):
#                     return isinstance(value, (int, float)) and value >= 0
                
           

#                 # Apply validation checks
#     def checkthedata_valid(self):
                
#                 try:
#                     df=pd.read_csv(self.data_ingestion_artificat_obj.dataset_file_path)
                    
        
#                     invalid_rows = df[
#                         (~df["sex"].apply(self.validate_sex)) |
#                         (~df["bmi"].apply(self.validate_bmi)) |
#                         (~df["children"].apply(self.validate_children)) |
#                         (~df["smoker"].apply(self.validate_smoker)) |
#                         (~df["region"].apply(self.validate_region)) |
#                         (~df["charges"].apply(self.validate_charges))
#                     ]

#                     # Display validation results

#                     if invalid_rows.empty:
#                         # print(invalid_rows)
#                         print("✅ Data is valid!")
#                         # print(type(invalid_rows))
#                         os.makedirs(self.datavalidation_obj.datavalidation_dir,exist_ok = True)


#                         valid_file_path=os.path.join(self.datavalidation_obj.datavalidation_dir,self.datavalidation_obj.valid_data_file_name)
#                         df.to_csv(valid_file_path,index=False)
#                         logging.info(f"successfully saved dataset data {valid_file_path}")

                        
#                     else:
#                         print("⚠️ Invalid data found:")
#                         invalid_file_path=os.path.join(self.datavalidation_obj.datavalidation_dir,self.datavalidation_obj.invalid_data_file_name)
#                         df.to_csv(invalid_file_path,index=False)
#                         logging.info(f"successfully saved dataset data {invalid_file_path}")
#                         # print(invalid_rows)
#                         df.drop(invalid_rows.index,inplace=True)


#                     Datavalidation_artfact=artifact_entity.DatavalidationArtifact(valid_Dataset_file_path=valid_file_path,invalid_Dataset_file_path=invalid_file_path)
#                     return Datavalidation_artfact
                
#                 except Exception as e:
#                  raise InsuranceException(e ,sys)







            
import os
import numpy as np
import sys
import pandas as pd
from source_code.logger import logging
from source_code.exception import InsuranceException
from source_code.entity import config_entity, artifact_entity

class Datatvalidation:
    def __init__(self, datavalidation_obj: config_entity.Datavalidationconfig, data_ingestion_artificat: artifact_entity.Dataingenstionartifact):
        try:
            self.datavalidation_obj = datavalidation_obj
            self.data_ingestion_artificat_obj = data_ingestion_artificat
        except Exception as e:
            raise InsuranceException(e, sys)

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

    # Method to check if data is valid
    def checkthedata_valid(self):
        try:
            df = pd.read_csv(self.data_ingestion_artificat_obj.dataset_file_path)
            excepted_coloum ={"age","sex","bmi","children","smoker","region","charges"}
            if excepted_coloum.issubset(df.columns):

            # Apply validation checks for all rows
                invalid_rows = df[
                    (~df["age"].apply(self.validate_sex)) |
                    (~df["sex"].apply(self.validate_sex)) |
                    (~df["bmi"].apply(self.validate_bmi)) |
                    (~df["children"].apply(self.validate_children)) |
                    (~df["smoker"].apply(self.validate_smoker)) |
                    (~df["region"].apply(self.validate_region)) |
                    (~df["charges"].apply(self.validate_charges))
                ]
                # print(invalid_rows)
                # Check if there are invalid rows
                if invalid_rows.empty:
                    print("✅ Data is valid!")
                    os.makedirs(self.datavalidation_obj.datavalidation_dir, exist_ok=True)

                    valid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.valid_data_file_name)
                    df.to_csv(valid_file_path, index=False)
                    logging.info(f"Successfully saved valid dataset at {valid_file_path}")
                else:
                    print("⚠️ Invalid data found:")
                    os.makedirs(self.datavalidation_obj.datavalidation_dir, exist_ok=True)

                    invalid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.invalid_data_file_name)


                    invalid_rows.to_csv(invalid_file_path, index=False)  # Save invalid rows separately
                    logging.info(f"Successfully saved invalid dataset at {invalid_file_path}")

                    # Remove invalid rows from the original DataFrame
                    df.drop(invalid_rows.index, inplace=True)

                    # Saving the cleaned data (with valid rows only)
                    valid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.valid_data_file_name)

                    df.to_csv(valid_file_path, index=False)
                    logging.info(f"Successfully saved cleaned dataset at {valid_file_path}")
            else:
                df=df[list(excepted_coloum)]
                invalid_rows = df[
                    (~df["age"].apply(self.validate_sex))|
                    (~df["sex"].apply(self.validate_sex)) |
                    (~df["bmi"].apply(self.validate_bmi)) |
                    (~df["children"].apply(self.validate_children)) |
                    (~df["smoker"].apply(self.validate_smoker)) |
                    (~df["region"].apply(self.validate_region)) |
                    (~df["charges"].apply(self.validate_charges))
                ]

                # Check if there are invalid rows
                if invalid_rows.empty:
                    print("✅ Data is valid!")
                    os.makedirs(self.datavalidation_obj.datavalidation_dir, exist_ok=True)

                    valid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.valid_data_file_name)
                    df.to_csv(valid_file_path, index=False)
                    logging.info(f"Successfully saved valid dataset at {valid_file_path}")
                else:
                    print("⚠️ Invalid data found:")
                    os.makedirs(self.datavalidation_obj.datavalidation_dir, exist_ok=True)

                    invalid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.invalid_data_file_name)


                    invalid_rows.to_csv(invalid_file_path, index=False)  # Save invalid rows separately
                    logging.info(f"Successfully saved invalid dataset at {invalid_file_path}")

                    # Remove invalid rows from the original DataFrame
                    df.drop(invalid_rows.index, inplace=True)

                    # Saving the cleaned data (with valid rows only)
                    valid_file_path = os.path.join(self.datavalidation_obj.datavalidation_dir, self.datavalidation_obj.valid_data_file_name)

                    df.to_csv(valid_file_path, index=False)
                    logging.info(f"Successfully saved cleaned dataset at {valid_file_path}")
                

            
            Datavalidation_artfact=artifact_entity.DatavalidationArtifact(valid_Dataset_file_path=valid_file_path)
            print(Datavalidation_artfact.valid_Dataset_file_path)
            return Datavalidation_artfact

        except Exception as e:
            raise InsuranceException(e, sys)
