import numpy as np 
import pandas as pd
import  os , sys ,joblib 
from source_code.logger import logging 
from source_code.exception import InsuranceException 
from source_code.entity import config_entity,artifact_entity
from sklearn.preprocessing import OneHotEncoder,StandardScaler,RobustScaler 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
logging.info("Model evaluation Start 📳")

class ModelEvaluation:
    def __init__(self,datatransformation_artifact:artifact_entity.DataTransFormArtifact,
                 ):
        try:
            self.datatransformation_artifact=datatransformation_artifact
            

        except Exception as e:
            raise InsuranceException(e ,sys)

