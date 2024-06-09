import os
import sys
from pathlib import Path
from utils.common import create_directories,read_csv,save_object
from dataclasses import dataclass
from exception.exception import customexception
from logger.logger import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def data_preprocessing(self):
        try:
            # reading data
            dataset_path = self.config.unzip_data_files
            dataframe = read_csv(dataset_path)
            
            logging.info("Data preprocessing started")
            
            # preprocessing on data
            dataframe.drop("id",axis=1,inplace=True)
            dataframe.drop(dataframe[(dataframe['price'] >= 10000) & (dataframe['carat'] > 0)  & (dataframe['carat'] < 0.9)].index,inplace=True)
            dataframe.drop(dataframe[(dataframe['x']<0.2) | (dataframe['y']<0.2) | (dataframe['z']<0.2)].index,inplace=True)
            
            # saving file in the data_transformation artifact
            preprocessed_data_path = self.config.preprocessed_data_files
            create_directories([preprocessed_data_path])
            
            file_path = os.path.join(preprocessed_data_path,"preprocessed_data.csv")
            dataframe.to_csv(file_path,index=False)
            
            
            # dependent and independent feature separation
            X = dataframe.drop('price',axis=1)
            y = dataframe['price'] 
            
            # preprocessing pipeline creation
            cat_cols = X.select_dtypes(include="object").columns
            nume_cols = X.select_dtypes(exclude="object").columns
            
            cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]
            color_categories = ["D","E","F","G","H","I","J"]
            clarity_categories = ["I1","SI1","SI2","VS2","VS1","VVS2","VVS1","IF"]
            
            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('scaler',StandardScaler())
                ]
            )
            categorical_pipline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))
                ]
            )
            
            # use column transformer to join the two pipelines
            # (name, transformer, columns)
            preprocessor = ColumnTransformer([
                ("Numeric Pipeline",numeric_pipeline,nume_cols),
                ("Categorical Pipeline",categorical_pipline,cat_cols)
            ])

            preprocessed_model_path = os.path.join(self.config.preprocessed_data_files,"preprocessor.pkl")
            logging.info(f"Saving preprocessor object at {preprocessed_model_path}")
            save_object(preprocessed_model_path,preprocessor)

            logging.info("Data preprocessing completed, preprocessing object return successfully")
            
            return preprocessor
        except Exception as e:
            raise customexception(e,sys)
    
    def data_transformation(self):
        try: 
            preprocessor_obj = self.data_preprocessing()
            
            logging.info("Data transformation started")
            
            create_directories([self.config.transform_data_files])
            
            dataset_path = os.path.join(self.config.preprocessed_data_files,"preprocessed_data.csv")
            dataframe = read_csv(dataset_path)
            X = dataframe.drop('price',axis=1)
            y = dataframe['price']
            
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
            
            X_train = preprocessor_obj.fit_transform(X_train)
            X_test = preprocessor_obj.transform(X_test)
            
            columns = list(dataframe.columns)
            print(columns)
            
            train_arr = np.c_[X_train,np.array(y_train)]
            train_df = pd.DataFrame(train_arr,columns=columns)
            train_df_path = os.path.join(self.config.transform_data_files,"transform_train.csv")
            train_df.to_csv(train_df_path,index=False)
            
            test_arr = np.c_[X_test,np.array(y_test)]
            test_df = pd.DataFrame(test_arr,columns=columns)
            test_df_path = os.path.join(self.config.transform_data_files,"transform_test.csv")
            test_df.to_csv(test_df_path,index=False)
            

            logging.info("Data transformation completed")
        except Exception as e:
            raise customexception(e,sys)