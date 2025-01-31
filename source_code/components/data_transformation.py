import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity,artifact_entity


class Datatransformation:
    def __init__(self,datatransfer_obj:config_entity.DataTranformation):
        try:
            self.datatransfer_obj=datatransfer_obj

            
        except Exception as e:
            raise InsuranceException(e,sys)
    def datatransfer(self):
        try:
            """
            this funtion is used to lable encoding 

            """
            df=pd.read_csv(self.datatransfer_obj.cleaning_dataset)
            df.shape




        except Exception as e:
            raise InsuranceException(e ,sys )