from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

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
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiated data transformation component")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data transformation completed successfully")
        print(data_transformation_artifact)
        logging.info("Model Training Started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training Completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)