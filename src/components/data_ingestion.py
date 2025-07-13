#data ingestion is where u collect and load data from various sources into ur system for further processing
import os #file usage
import sys
from src.exception import CustomException # if any execption call the file we made
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass #which is used to quickly create classes that store **configuration values** (like paths), without writing an explicit `__init__()` method.

#pipeline

from src.components.data_transformation import DataTransformation #preproccsing of the data (handling missing values,encoding,sclaing,etc)
from src.components.data_transformation import DataTransformationConfig #config class that holds paths like where to save preprocessor.pkl,input and output features
'''
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
'''
@dataclass # can direcly define my class varible without using __init__
class DataIngestionConfig: #holds paths for saving the raw, train, and test datasets.
    train_data_path: str=os.path.join('artifacts',"train.csv") #all the outputs stored in artifcat folder by data ingestion
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # can use any data source eg-mongodb,etc
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path, #all are in csv format
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
'''
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))'''



