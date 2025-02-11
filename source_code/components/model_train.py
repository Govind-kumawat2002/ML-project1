import numpy as np 
import pandas as pd
import  os , sys ,joblib 
from source_code.logger import logging 
from source_code.exception import InsuranceException 
from source_code.entity import config_entity,artifact_entity
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
class ModelTraning:
    def __init__(self,datatransformation_artifact:artifact_entity.DataTransFormArtifact,
                 modeltrainerconfig:config_entity.ModelTrainerConfig
                 ):
        try:
            self.datatransformation_artifact=datatransformation_artifact
            self.modeltrainerconfig=modeltrainerconfig

        except Exception as e:
            raise InsuranceException(e, sys)
    def declared_model(self,x,y):
        try:
            logging.info(f"fitting the model")
            xgr = XGBRegressor()
            xgr.fit(x,y)
            return xgr
        except Exception as e:
            raise InsuranceException(e,sys)
    def initiate_modelTrainer(self,):
        try:
            pass
        except Exception as e:
            raise InsuranceException(e,sys)




