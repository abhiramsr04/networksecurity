import sys
import os 
import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constants.training_pipeline import TARGET_COLUMN
from networksecurity.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact, data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
            self.imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def get_data_transformer_object(cls) -> Pipeline:
        logging.info("Entered the get_data_transformer_object method of Data Transformation class")
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"initiatized KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor: Pipeline = Pipeline([("imputer", imputer)])
            return processor
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info("Entered the initiate_data_transformation method of Data Transformation class")
        try:
            logging.info("Starting data transformation process")
            train_df = self.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = self.read_data(self.data_validation_artifact.valid_test_file_path)

            impute_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            impute_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            preprocessor = self.get_data_transformer_object()

            preprocessor_object = preprocessor.fit(impute_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(impute_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(impute_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature, target_feature_train_df.to_numpy()]
            test_arr = np.c_[transformed_input_test_feature, target_feature_test_df.to_numpy()]

            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)

            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            logging.info("Data transformation completed successfully")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

