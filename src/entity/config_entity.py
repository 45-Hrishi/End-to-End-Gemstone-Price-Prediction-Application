from dataclasses import dataclass
from pathlib import Path

# dataclass is used to stored the arguments and remembers it to not add more than this arguments.
dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    