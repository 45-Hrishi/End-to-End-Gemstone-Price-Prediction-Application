from config.configuration import ConfigurationManager
from components.model_trainer import ModelTraining
from exception.exception import customexception
from logger.logger import logging
import sys


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_training = ModelTraining(model_training_config)
        model_training.trainer()
        
if __name__=="__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        raise customexception(e,sys)