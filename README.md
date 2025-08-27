# 🔐 Network Security: Phishing Website Detection using Machine Learning

## 📌 Overview
This project implements an **end-to-end Machine Learning pipeline** for detecting phishing websites, with complete automation from **data ingestion to deployment**.  
It demonstrates expertise in **MLOps practices** such as experiment tracking, CI/CD integration, containerization, and cloud storage.

The solution is designed to be **production-ready**, modular, and scalable for real-world network security applications.

---

## ✨ Features
- **Automated Data Pipeline**: Data ingestion, validation, transformation, and feature engineering.  
- **Model Training & Evaluation**: Multiple ML models trained and evaluated on phishing detection dataset.  
- **Data Drift Detection**: Automatic validation using schema + drift reports (`report.yaml`).  
- **Experiment Tracking**: Versioned artifacts for reproducibility and comparison.  
- **Deployment Ready**: REST API (Flask/FastAPI) in `app.py`.    
- **Containerized Environment**: `Dockerfile` for portable deployment.  

---

## 📂 Project Structure
├── app.py # Web API for model inference
├── main.py # Entry point for running the ML pipeline
├── push_data.py # Pushes raw data to database/cloud
├── test_mongodb.py # MongoDB integration test
├── requirements.txt # Dependencies
├── setup.py # Package setup
├── Dockerfile # Docker containerization
├── .github/workflows/main.yml # CI/CD pipeline
├── Network_Data/phisingData.csv # Dataset
├── data_schema/schema.yaml # Schema definition for validation
├── networksecurity/
│ ├── components/ # Modular pipeline components
│ │ ├── data_ingestion.py
│ │ ├── data_validation.py
│ │ ├── data_transformation.py
│ │ ├── model_trainer.py
│ └── cloud/s3_syncer.py # Cloud (S3) sync utilities
├── Artifacts/ # Stored experiment outputs
├── final_model/ # Final trained model + preprocessor
└── logs/ # Logs for monitoring pipeline


---

## 🛠️ Tech Stack
- **Programming**: Python 3.10  
- **ML/DL**: Scikit-learn, NumPy, Pandas  
- **Data Validation**: YAML schema + drift detection  
- **Deployment**: Flask/FastAPI (`app.py`)  
- **Experiment Tracking & Versioning**: Custom artifacts, pickle models  
- **Containerization**: Docker   
- **CI/CD**: GitHub Actions  
- **Database**: MongoDB (for data storage & integration)

---

## 📊 Dataset
- **Source**: `Network_Data/phisingData.csv`  
- **Task**: Classify websites as *Phishing* or *Legitimate* based on extracted features.  
- **Preprocessing**: Handled via `data_transformation.py` (feature encoding, scaling, etc.).

---

## ⚙️ Workflow
1. **Data Ingestion**  
   - Load phishing dataset.  
   - Push to database/cloud (optional).  

2. **Data Validation**  
   - Schema check using `schema.yaml`.  
   - Data drift detection with report generation.  

3. **Data Transformation**  
   - Preprocessing pipeline (scaling, encoding, feature selection).  
   - Artifacts saved for reproducibility.  

4. **Model Training & Evaluation**  
   - Train ML models (Decision Trees, Random Forest, etc.).  
   - Evaluate on train/test sets.  
   - Save final model in `final_model/`.  

5. **Deployment**  
   - REST API using Flask/FastAPI (`app.py`).  
   - Containerized via `Dockerfile`.  
   - CI/CD pipeline automates build, test, and deploy.  

---

📈 Results

Achieved high accuracy in phishing detection (exact metrics depend on training run).

Data drift handled via automated validation pipeline.

Final trained model stored in final_model/model.pkl.

👤 Author

Abhiram S R (B.Tech, NITK Surathkal)

🌐 Portfolio: [link](https://abhiram-s-r-portfolio-delta.vercel.app/)

💼 LinkedIn: [link](https://www.linkedin.com/in/abhiram-s-r/)

