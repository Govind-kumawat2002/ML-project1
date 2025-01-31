# eske ander bhi variable n=banye jate hai 
# jo durring the data_ingestion variable 
from dataclasses import dataclass
@dataclass
class Dataingenstionartifact:
    Dataset_file_path:str
    total_Train_file_path:str
    total_Test_file_path:str
@dataclass
class Dataclean:
    clean_dataset_file_path:str
    total_train_file_path:str
    total_test_file_path:str

@dataclass
class Datavalidation:
    Dataset_file_path:str