from config.configuration import ModelPredictionConfig
from utils.common import load_object
from logger.logger import logging
from exception.exception import customexception
from utils.pred_validation import DataValidation
import pandas as pd
import sys

class ModelPrediction:
    def __init__(self,config:ModelPredictionConfig):
        self.config = config
        self.schema_file = "schema.json"
    
    def predict(self,input_data_dict):
        try:
            validator = DataValidation(self.schema_file)
            isvalidated = validator.validate(input_data_dict)
            if isvalidated:
                preprocessor = load_object(self.config.preprocessor_obj_path)
                model = load_object(self.config.model_path)
                
                input_df = pd.DataFrame([input_data_dict])
                transform_data = preprocessor.transform(input_df)
                print(transform_data)
                
                prediction_result = model.predict(transform_data)
                print(prediction_result)
                
                logging.info(f"Prediction result : {prediction_result}")
                return prediction_result
            else:
                logging.error("Data validation error")
            
        except Exception as e:
            raise customexception(e,sys)