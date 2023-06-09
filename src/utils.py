# read a data  from database, save from cloud etc

import os
import sys
import pandas as pd
import numpy as np
import logging
import pickle
from logger import logging
from src.exception import CustomExpression_ANIL

def save_object(file_path:str,obj):
    try:
        logging.info(f'saving object to a pickle file having path:{file_path}')
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException_ANIL(e,sys)