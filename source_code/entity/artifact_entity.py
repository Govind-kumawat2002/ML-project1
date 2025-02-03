# eske ander bhi variable n=banye jate hai 
# jo durring the data_ingestion variable 
from dataclasses import dataclass
@dataclass
class Dataingenstionartifact:
    dataset_file_path:str
    train_file_path:str
    test_file_path:str
# @dataclass
# class Datacleanartifact:
#     clean_dataset_file_path:str
#     total_train_file_path:str
#     total_test_file_path:str

@dataclass
class DatavalidationArtifact:
    valid_Dataset_file_path:str
    # invalid_Dataset_file_path:str


@dataclass
class DatacleaningArtifact:
    clean_file_path:str
