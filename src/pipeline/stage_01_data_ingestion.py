from config.configuration import ConfigurationManager
from components.data_ingestion import DataIngestion
from exception.exception import customexception
from logger.logger import logging
import sys


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_dataingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
        
if __name__=="__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        raise customexception(e,sys)