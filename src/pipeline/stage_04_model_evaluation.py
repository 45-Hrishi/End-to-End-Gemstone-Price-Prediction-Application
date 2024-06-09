from config.configuration import ConfigurationManager
from components.model_evaluation import ModelEvaluation
from exception.exception import customexception
from logger.logger import logging
import sys


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.model_evaluate()
        
if __name__=="__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        raise customexception(e,sys)