import os
import sys
from logger.logger import logging
from pathlib import Path
from dataclasses import dataclass
from exception.exception import customexception
from utils.common import create_directories,save_object,read_yaml,evaluate_model,get_transform_data
from sklearn.linear_model import LinearRegression,ElasticNet,Ridge,Lasso
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from entity.config_entity import ModelTrainingConfig

from utils.common import evaluate_model
class ModelTraining:
    def __init__(self,config:ModelTrainingConfig):
        self.config = config
        
    def best_model(self):
        try:
            logging.info("Searching for best model with highest accuracy")
            X_train,y_train,X_test,y_test = get_transform_data(path_to_folder=self.config.transform_data_path)
            models = {
                "LinearRegression":LinearRegression(),
                "LassoRegression":Lasso(),
                "RidgeRegression":Ridge(),
                "ElasticNet":ElasticNet(),
                "XGBoost":XGBRegressor(),
                "RandomForest":RandomForestRegressor()
            }
            report = evaluate_model(X_train,y_train,X_test,y_test,models)
            # print(report)
            model_dict = sorted(report.items(),key=lambda item:item[1],reverse=True)
            print(model_dict)
            model_obj,accuracy = model_dict[0]
            logging.info(f"{model_obj} has highest accuracy of {accuracy}")
            return model_obj,X_train,y_train
        except Exception as e:
            raise customexception(e,sys)
        
    def trainer(self):
        model_obj,X_train,y_train = self.best_model()
        model_obj = model_obj.fit(X_train,y_train)
        save_object(self.config.trained_model_path,model_obj)