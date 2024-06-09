from logger.logger import logging
from config.configuration import ConfigurationManager
from components.prediction import ModelPrediction
from exception.exception import customexception
from utils.pred_validation import CustomData
import sys

try:
    logging.info("Model prediction started")
    config = ConfigurationManager()
    model_prediction_Config = config.get_prediction_config()
    model_prediction = ModelPrediction(model_prediction_Config)
    custom_data_obj = CustomData()
    input_data =custom_data_obj.get_data_as_dataframe()
    model_prediction.predict(input_data)
    logging.info("Model prediction completed")
except Exception as e:
    raise customexception(e,sys)