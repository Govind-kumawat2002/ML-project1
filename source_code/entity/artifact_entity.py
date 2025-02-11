# eske ander bhi variable n=banye jate hai 
# jo durring the data_ingestion variable 
from dataclasses import dataclass
@dataclass
class Dataingenstionartifact:
    dataset_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DatavalidationArtifact:
    valid_Dataset_file_path:str
    # invalid_Dataset_file_path:str


@dataclass
class DatacleaningArtifact:
    clean_file_path:str

@dataclass
class DataTransFormArtifact:
    onehot_data_file_path:str 
    onehot_encoder_model_path:str 

    scaler_data_file_path:str 
    scaler_model_path:str 


@dataclass
class ModelTrainerArtifact:
    model_dir_path_with_default_parm_standard_data:str
    model_dir_path_with_default_parm_nonstandard_data:str

    model_dir_path_tuned_model_standard_data:str
    model_dir_path_tuned_model_nonstandard_data:str

