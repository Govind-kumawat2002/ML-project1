# import os 
# import numpy as np 
# import sys
# import pandas as pd 
# from source_code.logger import logging
# from source_code.exception import InsuranceException
# # load dataset from dir 
# from source_code.entity import config_entity, artifact_entity
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
# from sklearn.impute import SimpleImputer
# from sklearn.decomposition import PCA

# class Datatransformatio:
#     def __init__(self,datatransfromation_artifact:artifact_entity.DatacleaningArtifact):
#         try:
#             self.datatransfromation_artifact=datatransfromation_artifact
#             self.dataset=pd.read_csv(datatransfromation_artifact.clean_file_path)
#         except Exception as e:
#             raise InsuranceException(e,sys)
#     def transform_data(self,df, scaling_method='standard', encode_categorical=True, impute_missing=True, apply_pca=False, n_components=2):
#         """
#         Transforms the given dataframe by handling missing values, encoding categorical features, scaling, and PCA.

#         Parameters:
#         - df (pd.DataFrame): The input dataframe.
#         - scaling_method (str): 'standard' (Z-score) or 'minmax' (Min-Max scaling).
#         - encode_categorical (bool): Whether to encode categorical variables.
#         - impute_missing (bool): Whether to impute missing values.
#         - apply_pca (bool): Whether to apply PCA for dimensionality reduction.
#         - n_components (int): Number of components for PCA.

#         Returns:
#         - pd.DataFrame: Transformed dataframe.
#         """

#         df = self.dataset.copy()

#         # Handle missing values
#         if impute_missing:
#             num_imputer = SimpleImputer(strategy='mean')  # Fill numeric columns with mean
#             cat_imputer = SimpleImputer(strategy='most_frequent')  # Fill categorical columns with mode
            
#             for col in df.select_dtypes(include=['number']).columns:
#                 df[col] = num_imputer.fit_transform(df[[col]])
            
#             for col in df.select_dtypes(include=['object', 'category']).columns:
#                 df[col] = cat_imputer.fit_transform(df[[col]])

#         # Encode categorical variables
#         if encode_categorical:
#             categorical_cols = df.select_dtypes(include=['object', 'category']).columns
#             encoder = OneHotEncoder(drop='first', sparse=False)
#             encoded_cols = encoder.fit_transform(df[categorical_cols])
#             df = df.drop(columns=categorical_cols)
#             df = pd.concat([df, pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_cols))], axis=1)

#         # Scaling
#         scaler = StandardScaler() if scaling_method == 'standard' else MinMaxScaler()
#         numerical_cols = df.select_dtypes(include=['number']).columns
#         df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

#         # Apply PCA if needed
#         if apply_pca:
#             pca = PCA(n_components=n_components)
#             df_pca = pca.fit_transform(df)
#             df = pd.DataFrame(df_pca, columns=[f'PC{i+1}' for i in range(n_components)])

#         return df

#     # Example usage
    


#     transformed_data = transform_data(df, scaling_method='minmax', encode_categorical=True, impute_missing=True, apply_pca=False)
#     print(transformed_data)
import os
import numpy as np
import sys
import pandas as pd
from source_code.logger import logging
from source_code.exception import InsuranceException
from source_code.entity import config_entity, artifact_entity
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

class DataTransformation:
    def __init__(self, datatransformation_artifact: artifact_entity.DatacleaningArtifact):
        """
        Initializes the DataTransformation class.

        :param datatransformation_artifact: Object containing paths for cleaned data.
        """
        try:
            self.datatransformation_artifact = datatransformation_artifact
            self.dataset = pd.read_csv(datatransformation_artifact.clean_file_path)
        except Exception as e:
            raise InsuranceException(e, sys)

    def transform_data(self, scaling_method='standard', encode_categorical=True, impute_missing=True, apply_pca=False, n_components=2):
        """
        Transforms the dataset by handling missing values, encoding categorical features, scaling, and PCA.

        Parameters:
        - scaling_method (str): 'standard' (Z-score) or 'minmax' (Min-Max scaling).
        - encode_categorical (bool): Whether to encode categorical variables.
        - impute_missing (bool): Whether to impute missing values.
        - apply_pca (bool): Whether to apply PCA for dimensionality reduction.
        - n_components (int): Number of components for PCA.

        Returns:
        - pd.DataFrame: Transformed dataframe.
        """

        df = self.dataset.copy()
#         print(df.info())

#         # Handle missing values
        # if impute_missing:
        #     num_imputer = SimpleImputer(strategy='mean')  # Fill numeric columns with mean
        #     cat_imputer = SimpleImputer(strategy='most_frequent')  # Fill categorical columns with mode
            
        #     for col in df.select_dtypes(include=['number']).columns:
        #         df[col] = num_imputer.fit_transform(df[[col]])
            
        #     for col in df.select_dtypes(include=['object', 'category']).columns:
        #         df[col] = cat_imputer.fit_transform(df[[col]])
   
        print(df)
        print("run this funtion ")


#         # Encode categorical variables
#         if encode_categorical:
#             categorical_cols = df.select_dtypes(include=['object', 'category']).columns
#             if len(categorical_cols) > 0:
#                 encoder = OneHotEncoder(drop='first', sparse=False)
#                 encoded_cols = encoder.fit_transform(df[categorical_cols])
#                 df = df.drop(columns=categorical_cols)
#                 df = pd.concat([df, pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_cols))], axis=1)

#         # Scaling
#         scaler = StandardScaler() if scaling_method == 'standard' else MinMaxScaler()
#         numerical_cols = df.select_dtypes(include=['number']).columns
#         df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

#         # Apply PCA if needed
#         if apply_pca:
#             pca = PCA(n_components=n_components)
#             df_pca = pca.fit_transform(df)
#             df = pd.DataFrame(df_pca, columns=[f'PC{i+1}' for i in range(n_components)])

#         return df

# # Example usage
# if __name__ == "__main__":
#     # Assume artifact_entity.DatacleaningArtifact has a valid `clean_file_path`
#     try:
#         datatransformation_artifact = artifact_entity.DatacleaningArtifact(clean_file_path="path_to_cleaned_data.csv")
#         transformer = DataTransformation(datatransformation_artifact)
#         transformed_data = transformer.transform_data(scaling_method='minmax', encode_categorical=True, impute_missing=True, apply_pca=False)
#         print(transformed_data.head())
#     except Exception as e:
#         print(f"Error: {e}")
