from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiated data ingestion component")
        dataingestion.initiate_data_ingestion()
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_vallidation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiated data validation component")
        data_vallidation.initiate_data_validation()
        data_validation_artifact = data_vallidation.initiate_data_validation()
        logging.info("Data validation completed successfully")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)