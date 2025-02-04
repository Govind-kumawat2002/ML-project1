from source_code.logger import logging 
from source_code.exception import InsuranceException 
from source_code.entity import config_entity,artifact_entity
from sklearn.preprocessing import OneHotEncoder,StandardScaler,RobustScaler 
import  os , sys ,joblib
import numpy as np 
import pandas as pd 

class DataTransformation:
    def __init__(self,data_transformation_config:config_entity.DataTransFormationConfig,
                    data_cleaning_artifact:artifact_entity.DatacleaningArtifact):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_cleaning_artifact = data_cleaning_artifact
        except Exception as e:
            raise InsuranceException(e,sys)


    def split_cat_num(self,df:pd.DataFrame)->pd.DataFrame:
        try:
            cat_df = df.select_dtypes(include="O")
            num_df = df.select_dtypes(exclude="O")
            return cat_df,num_df 
        except Exception as e:
            raise InsuranceException(e,sys)

    def transform_catgorical(self,cat_df: pd.DataFrame)-> tuple[pd.DataFrame, OneHotEncoder]:
        try:
            onehot_encoder = OneHotEncoder(drop='first')
            transformed_data = onehot_encoder.fit_transform(cat_df)
            df = pd.DataFrame(transformed_data.toarray(),columns=onehot_encoder.get_feature_names_out())
            return df , onehot_encoder  
        except Exception as e:
            raise InsuranceException(e,sys)

    def standardize_data(self,df:pd.DataFrame)-> tuple[pd.DataFrame, RobustScaler]:
        try:
            scaler = RobustScaler() 
            transform_df = scaler.fit_transform(df)
            return transform_df,scaler 
        except Exception as e:
            raise InsuranceException(e,sys)

    def transform_initiate(self)->artifact_entity.DataTransFormArtifact:
        try:
            df = pd.read_csv(self.data_cleaning_artifact.clean_file_path)
            cat_df,num_df = self.split_cat_num(df=df)

            cat_df_transormed,onehote_encoder = self.transform_catgorical(cat_df=cat_df)
            merged_df = pd.concat([num_df,cat_df_transormed],axis=1)
            logging.info("onehot encoding transformed")

            standardized_data, scaler = self.standardize_data(df=merged_df.drop("charges",axis=1))
            standardized_data = np.hstack([standardized_data, np.array(merged_df['charges']).reshape(-1, 1)])
            column_name_ls = list(merged_df.columns)
            column_name_ls.remove('charges')
            column_name_ls.append('charges')
            standardized_data = pd.DataFrame(standardized_data,columns=column_name_ls)

            logging.info("Robust scaler trnasormation")


            #save onehot 
            os.makedirs(self.data_transformation_config.onehotedata_dir,exist_ok=True)
            os.makedirs(self.data_transformation_config.standardized_dir,exist_ok=True)

            merged_df.to_csv(self.data_transformation_config.one_hot_data_file_path,index=False)
            joblib.dump(onehote_encoder,self.data_transformation_config.onehote_encoder_model_path)
            logging.info("saved onehot encoder data")

            #save scaled
            
            standardized_data.to_csv(self.data_transformation_config.scaled_data_file_path,index=False)
            joblib.dump(scaler,self.data_transformation_config.scaler_model_path)
            logging.info('data scaling done')


            data_transformation_artifact = artifact_entity.DataTransFormArtifact(
                                onehot_data_file_path=self.data_transformation_config.one_hot_data_file_path, 
                                onehot_encoder_model_path=self.data_transformation_config.onehote_encoder_model_path,
                                scaler_data_file_path=self.data_transformation_config.scaled_data_file_path,
                                scaler_model_path=self.data_transformation_config.scaler_model_path
            )

            logging.info("Data tranformation Done ✅")
            return data_transformation_artifact

        except Exception as e:
            raise InsuranceException(e,sys)