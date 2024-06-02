import os 
import sys
import pandas as pd
import numpy as np
import pickle
from logger.logger import logging
from exception.exception import customexception
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path,obj):
    try:
        #getting the name of directory from file_path and then create it.
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise customexception(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(model.values())[i]
            model.fit(X_train,y_train)
            
            y_pred = model.predict(X_test)
            #evaluation of model
            r2_score = r2_score(y_test,y_pred)
            
            model_name = list(model.keys())[i]
            report[model_name] = r2_score
        return report
            
    except Exception as e:
        logging.info("Exception occured while evaluating model")
        customexception(e,sys)
        
        
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info("Exception occured in load_object function")
        raise customexception(e,sys)