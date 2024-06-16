from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.logger.logger import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_transformation import DataTransformationPipeline
from src.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='GemstonePricePrediction_Pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 6, 16),
    catchup=False,
)

def DataIngestion():
    # data ingestion code
    STAGE_NAME = "Stage Data Ingestion"
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logging.exception(e)
        raise e

def DataTransformation():
    # data transformation code
    STAGE_NAME = "Stage Data Transformation" 
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logging.exception(e)
        raise e

def ModelTraining():
    # model training code
    STAGE_NAME = "Stage Model Training"
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logging.exception(e)
        raise e

def ModelEvaluation():
    # model evaluation code
    STAGE_NAME = "Stage Model Evaluation"
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logging.exception(e)
        raise e

ingest_task = PythonOperator(
    task_id='DataIngestion',
    python_callable=DataIngestion,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='DataTransformation',
    python_callable=DataTransformation,
    dag=dag,
)

train_task = PythonOperator(
    task_id='ModelTraining',
    python_callable=ModelTraining,
    dag=dag,
)

evaluate_task = PythonOperator(
    task_id='ModelEvaluation',
    python_callable=ModelEvaluation,
    dag=dag,
)

ingest_task >> transform_task >> train_task >> evaluate_task
