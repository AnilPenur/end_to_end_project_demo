# Step - 1: data reading convrt data into train test and validation
# From local source and mongo db


import os
import sys
from src.exception import CustomException_ANIL
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
# dataclass is used to create class variables without use of constructors
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation,DataTransformationConfig
 
# INPUT 
# we need to save trained data, test data and raw data that is saved within a class

@dataclass   #using dataclass we do not need variables to be defined withion constructor
class DataIngestionConfig:
    train_data_set:str = os.path.join('artifacts','train.csv')
    test_data_set:str = os.path.join('artifacts','test.csv')
    raw_data_set:str = os.path.join('artifacts','data.csv')
        
        
class Data_ingestion:
    def ___init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Entered data ingestion initiation method')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('dataset is read as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_set),exist_ok = True)
            logging.info('directory artifacts has been created')
            
            train_set , test_set = train_test_split(df, test_size=0.25, random_state = 42)
            logging.info('dataset is splitted into train and test')
            
            df.to_csv(self.ingestion_config.raw_data_set, index= False, header = True)
            train_set.to_csv(self.ingestion_config.train_data_set, index= False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_set, index= False, header = True)
            logging.info('raw, train and test data set has been saved to files')
            
            return(
                self.ingestion_config.train_data_set,
                self.ingestion_config.test_data_set
            )
            
        except Exception as e:
            raise CustomException_ANIL(e,sys)
            
            
if __name__='__main__':
    obj = Data_ingestion()
    train_path,test_path = obj.initiate_data_ingestion()
    
    data_transformation_obj = DataTransformation()
    data_transformation_obj.initiate_data_transformation(train_path= train_path, test_path= test_path)
    
        