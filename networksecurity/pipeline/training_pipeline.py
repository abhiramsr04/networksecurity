import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import ( TrainingPipelineConfig,
                                                  DataIngestionConfig,
                                                  DataTransformationConfig,
                                                  DataValidationConfig,
                                                  ModelTrainerConfig
                                                  )

from networksecurity.entity.artifact_entity import (DataIngestionArtifact,
                                                    DataTransformationArtifact,
                                                    DataValidationArtifact,
                                                    ModelTrainerArtifact)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
            logging.info("Start data Ingestion")
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e

    