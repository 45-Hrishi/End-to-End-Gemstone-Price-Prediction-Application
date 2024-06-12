import os
import zipfile
from utils.common import create_directories
from logger.logger import logging
from exception.exception import customexception
import sys
from pathlib import Path
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv
from entity.config_entity import DataIngestionConfig

load_dotenv()

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        try:
            download_dir = self.config.local_data_file
            root_dir = self.config.root_dir
            create_directories([self.config.root_dir])
            
            # authenticate with kaggle
            os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
            os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
            api = KaggleApi()
            api.authenticate()
            logging.info("Authentication succesful")
            api.competition_download_files('playground-series-s3e8', path=root_dir)
            
            for _file in os.listdir("artifacts/data_ingestion"):
                if _file == "playground-series-s3e8.zip":
                    current_path = os.path.join("artifacts/data_ingestion",_file)
                    new_path= os.path.join("artifacts/data_ingestion","data.zip")
                    os.rename(current_path,new_path)
                    break
                
            logging.info(f"Downloading data into the {download_dir}")
        except Exception as e:
            raise customexception(e,sys)
            
    def extract_zipfile(self):
        unzip_path = Path(self.config.unzip_dir)
        create_directories([unzip_path])
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        req_files = ["train.csv","test.csv"]
        for file_ in os.listdir(self.config.root_dir):
            if not file_ in req_files:
                file_path = os.path.join(self.config.root_dir,file_)
                os.remove(file_path)
            
        logging.info("Unzipping of data completed")