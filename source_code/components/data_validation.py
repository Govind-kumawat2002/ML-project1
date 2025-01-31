import os 
import numpy as np 
import sys
import pandas as pd 
from source_code.logger import logging
from source_code.exception import InsuranceException
# load dataset from dir 
from source_code.entity import config_entity,artifact_entity
artifact_entity.Datavalidation.Dataset_file_path

class Validation:
    def __init__(self,datavalidationconfig:config_entity.Datavalidationconfig,
                 dataingestionArtifact:artifact_entity.Dataingenstionartifact):

        try:
            self
            pass

            
        except Exception as e:
            raise InsuranceException(e ,sys )