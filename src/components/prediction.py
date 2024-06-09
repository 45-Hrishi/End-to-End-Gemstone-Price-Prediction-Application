from config.configuration import ModelPredictionConfig
from utils.common import load_object
from logger.logger import logging
from exception.exception import customexception
import sys

class ModelPrediction:
    def __init__(self,config:ModelPredictionConfig):
        self.config = config
    
    def predict(self,input_data):
        try:
            preprocessor = load_object(self.config.preprocessor_obj_path)
            model = load_object(self.config.model_path)
            
            transform_data = preprocessor.transform(input_data)
            print(transform_data)
            
            prediction_result = model.predict(transform_data)
            print(prediction_result)
            
            logging.info(f"Prediction result : {prediction_result}")
            return prediction_result
            
        except Exception as e:
            raise customexception(e,sys)