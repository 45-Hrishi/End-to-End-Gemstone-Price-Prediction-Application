import os
import sys
import mlflow
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from logger.logger import logging
from exception.exception import customexception
from dataclasses import dataclass
from pathlib import Path
from utils.common import create_directories,read_yaml,load_object,read_csv,save_json
from entity.config_entity import ModelEvaluationConfig
import mlflow

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
    
    def evaluate(self):
        try:
            logging.info("Loading the model")
            model_path = self.config.trained_model_path
            model_obj = load_object(model_path)
            
            logging.info("Loading the testing data")
            test_data_path = os.path.join(self.config.test_data_path,"transform_test.csv")
            test_df = read_csv(test_data_path)
            
            X_test = test_df.drop('price',axis=1)
            y_test = test_df['price']
            
            logging.info("Evaluating data")
            y_pred = model_obj.predict(X_test)
            
            
            mse = mean_squared_error(y_test,y_pred)
            logging.info(f"Mean squared error of model is: {mse}")
            mae = mean_absolute_error(y_test,y_pred)
            logging.info(f"Mean absolute error of model is: {mae}")
            score_r2 = r2_score(y_test,y_pred)
            logging.info(f"r2 score of model is: {score_r2}")
            
            logging.info("Storing metrics into json file")
            metrics = {"MSE":mse,"MAE":mae,"r2 score":score_r2}
            json_filepath = Path(self.config.metrics_json_path)
            print(json_filepath)
            save_json(json_filepath,metrics)
        except Exception as e:
            raise customexception(e,sys)
        
    def log_into_mlflow(self):
        pass