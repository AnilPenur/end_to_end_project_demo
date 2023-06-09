# Step - 2: transformation of data
# how to handel label encode, OneHot encoding
# even handle missing values and all


import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd 
from sklearn.compose import column_transfoermer
from sklearn.pipeline import Pipeline

from src.utils import save_object
from src.logger import logging
from src.exception import CustomException_ANIL



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join('artifacts','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        logging.info('initiated get_data_transformer_object method')
        try:
            num_columns=['reading_score','writing_score']
            cat_columns=[
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch',
                'test_preparation_course'  
            ]
            
            num_pipeline = Pipeline(
                [
                    ('MisiingImputer',SimpleImputer(strategy='median')),
                    ('standard_scaler',StandardScaler())
                ]
            )
            
            cat_pipeline = Pipeline(
                [('Missing_imputer',SimpleImputer(strategy='most_frequent')),
                ('One hot encoder',OneHotEncoder()),
                 ('standard scaler',StandardScaler())
                ]
            )
            
            preprocess = ColumnTransformer(
                [('numerical_column',num_pipeline,num_columns),
                ('categorical_pipeline',cat_pipeline,cat_columns)]
            )
            
            return preprocess
        
        except Exception as e:
            raise CustomException_ANIL(e,sys)
            
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('Train and test data read complete')
            
            logging.info('Applying preprocessing to train ande test dataset')
            preprocess_obj = self.get_data_transformer_object()
            
            target_column = 'math_score'
            num_columns = ['reading_score','writing_score']
            
            input_feature_train_df = train_df.drop(columns=target_column,axis=1)
            target_feature_train_df = train_df[target_column]
            
            input_feature_test_df = test_df.drop(columns=target_column,axis=1)
            target_feature_test_df = test_df[target_column]
            
            
            input_feature_train_transformed = preprocess_obj.fit_transform(input_feature_train_df)
            input_feature_test_transformed = preprocess_obj.transform(input_feature_test_df)
            
            #remerge train and test (target + transformed data)
            train_df_transformed = np.c_[input_feature_train_transformed,np.array(target_feature_train_df)]
            test_df_transformed = np.c_[input_feature_test_transformed,np.array(target_feature_test_df)]
            
            logging.info('Saving the preprocesseed train and test dataset')
            
            save_object( 
                file_path = self.data_transformation_config.preprocessor_obj_file_path
                obj = preprocess_obj
            )
            logging.info('Saved the preprocessed object pickle file')
            
            return(
                train_df_transformed,
                test_df_transformed,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
            
        except Exception as e:
            raise CustomException_ANIL(e,sys)
            
