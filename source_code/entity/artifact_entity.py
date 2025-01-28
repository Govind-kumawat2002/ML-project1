# eske ander bhi variable n=banye jate hai 
# jo durring the data_ingestion variable 
from dataclasses import dataclass
@dataclass
class Dataingenstionartifact:
    Dataset_file_path:str
    Train_file_path:str
    Test_file_path:str