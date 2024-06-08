from config.configuration import ConfigurationManager
from components.data_transformation import DataTransformation
from exception.exception import customexception
from logger.logger import logging
import sys


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_datatransformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.data_transformation()
        
if __name__=="__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        raise customexception(e,sys)