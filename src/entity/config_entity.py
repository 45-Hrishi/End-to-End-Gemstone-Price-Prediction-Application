from dataclasses import dataclass
from pathlib import Path

# dataclass is used to stored the data arguments and frozen=True it to not add more than this arguments.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file:Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    unzip_data_files: Path
    preprocessed_data_files: Path
    transform_data_files: Path
    
@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    trained_model_path: Path
    transform_data_path: Path
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    trained_model_path: Path
    test_data_path: Path
    metrics_json_path: Path
    
@dataclass(frozen=True)
class ModelPredictionConfig:
    preprocessor_obj_path: Path
    model_path: Path