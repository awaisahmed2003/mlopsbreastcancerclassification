**MLOps-chest-cancer-classification**


This project focuses on building an end-to-end machine learning pipeline for chest cancer classification, leveraging MLflow and DVC for streamlined ML lifecycle management. The pipeline is deployed using GitHub and Docker, with the application hosted in a Flask environment.

**Key Components**

Data Ingestion: Importing and preprocessing the dataset.

Preparing Model: Feature engineering and selection.

Training Model: Model training and hyperparameter tuning.

Model Evaluation: Evaluating model performance and generating metrics.

Prediction: An interactive pipeline allowing users to make predictions based on the trained model.



**Workflows**

Update config.yaml

Update params.yaml

Update the entity

Update the configuration manager in src/config

Update the components

Update the pipeline

Update main.py

Update dvc.yaml



**Prediction (Docker Local Deployment**)

To allow anyone to run the model locally using Docker:

Step 1: Build Docker Image
bash
Copy
Edit
docker build -t chest-cancer-classifier .
Step 2: Run Prediction on an Image
bash
Copy
Edit
docker run -v ${PWD}:/app chest-cancer-classifier python predict.py /app/sample.jpg
Note: Replace sample.jpg with your desired image.



**Classes**

The model currently supports 2 classes:

malignant

normal

Your training data directory should be structured as follows:

css
Copy
Edit
data/
├── malignant/
└── normal/


**To Train the Model**

Run the following command to ingest data, train the model, and save the trained model to artifacts/:

bash
Copy
Edit
docker run chest-cancer-classifier python main.py
After Training, Run the Evaluation Pipeline
bash
Copy
Edit
docker run chest-cancer-classifier python src/cnnClassifier/pipeline/stage_04_model_evaluation.py
Feel free to adjust the instructions based on any further changes to your project structure or deployment preferences. Let me know if you need additional modifications!


