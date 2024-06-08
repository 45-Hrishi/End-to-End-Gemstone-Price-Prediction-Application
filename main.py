from src.logger.logger import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_transformation import DataTransformationPipeline
from src.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Stage Data Ingestion"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Stage Data Transformation" 
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Stage Model Training"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Stage Model Evaluation"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logging.exception(e)
    raise e