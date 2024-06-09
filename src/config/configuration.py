from constants import CONFIG_FILE_PATH
from utils.common import create_directories,read_yaml
from entity.config_entity import (DataIngestionConfig,DataTransformationConfig,
                                  ModelTrainingConfig,ModelEvaluationConfig,ModelPredictionConfig)
import os

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])
        
    def get_dataingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_datatransformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            unzip_data_files = config.unzip_data_files,
            preprocessed_data_files = config.preprocessed_data_files,
            transform_data_files = config.transform_data_files
        )
        
        return data_transformation_config
    
    def get_model_trainer_config(self)->ModelTrainingConfig:
        training_config = self.config.model_training
        transform_config = self.config.data_transformation
        
        create_directories([training_config.root_dir])
        model_trainer_config = ModelTrainingConfig(
            root_dir = training_config.root_dir,
            trained_model_path=training_config.model_path,
            transform_data_path=transform_config.transform_data_files
        )
        return model_trainer_config
    
    def get_evaluation_config(self)->ModelEvaluationConfig:
        training_config = self.config.model_training
        datatransform_config = self.config.data_transformation
        model_evaluation_config = self.config.model_evaluation
        
        create_directories([model_evaluation_config.root_dir])
        evaluation_config = ModelEvaluationConfig(
            trained_model_path=training_config.model_path,
            test_data_path=datatransform_config.transform_data_files,
            metrics_json_path=model_evaluation_config.metrics_path
        )
        return evaluation_config
    
    def get_prediction_config(self)->ModelPredictionConfig:
        training_config = self.config.model_training
        datatransform_config = self.config.data_transformation
        
        preprocessor_path = os.path.join(datatransform_config.preprocessed_data_files,"preprocessor.pkl")
        
        prediction_config = ModelPredictionConfig(
            preprocessor_obj_path=preprocessor_path,
            model_path=training_config.model_path
        )
        
        return prediction_config