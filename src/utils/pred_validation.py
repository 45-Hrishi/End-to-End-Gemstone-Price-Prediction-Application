from logger.logger import logging
from exception.exception import customexception
import pandas as pd
import sys
import json

class DataValidation:
    def __init__(self,schema_file):
        with open(schema_file,'r') as f:
            schema = json.load(f)
            self.schema = schema['columns']
            
    def validate(self,data):
        flag = True
        for key, expected_type in self.schema.items():
            if key not in data:
                logging.error(f"Missing key {key}")
                flag=False
            
            value = data[key]
            if expected_type=="float":
                if not isinstance(value,(float,int)):
                    logging.error(f"Incorrect type for {key}: expected {expected_type}, got {type(value).__name__}")
                    flag = False      
            elif expected_type =="str":
                if not isinstance(value,str):
                    logging.error(f"Incorrect type for {key}: expected {expected_type}, got {type(value).__name__}")
                    flag=False
            else:
                logging.error("Unsupported type in schema")
                flag=False
                
        return flag
        