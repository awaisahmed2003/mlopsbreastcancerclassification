# MLOps Chest Cancer Classification

This project implements an end-to-end machine learning pipeline for classifying chest cancer using image data. The pipeline is containerized using Docker, allowing easy local deployment and inference.

---

## 🔹 Key Components

- **Data Ingestion** – Load and preprocess image data from specified directories.
- **Model Preparation** – Load and update a pre-trained CNN model.
- **Training** – Train the model using a training-validation split.
- **Evaluation** – Evaluate performance and save metrics.
- **Prediction** – Run inference on new images using the trained model.

---

## 🔹 Workflow

1. Update `config.yaml` with directory paths and filenames.
2. Update `params.yaml` to control hyperparameters like image size, batch size, and epochs.
3. Update `entity` classes in `src/entity/`.
4. Modify configuration manager in `src/configuration/`.
5. Update components under `src/components/`.
6. Adjust pipeline stages in `src/pipeline/`.
7. Run `main.py` to execute the full training pipeline.

---

## 🔹 Docker Deployment

### Step 1: Build Docker Image

```bash
docker build -t chest-cancer-classifier .
```

### Step 2: Predict Using an Image

```bash
docker run -v ${PWD}:/app chest-cancer-classifier python predict.py /app/sample.jpg
```

> Replace `sample.jpg` with your own image path.

---

## 🔹 Classes

This model currently supports **2 image classes**:

- `malignant`
- `normal`

### Folder Structure

```
data/
├── malignant/
│   ├── img1.jpg
│   └── ...
└── normal/
    ├── img1.jpg
    └── ...
```

---

## 🔹 To Train the Model

```bash
docker run chest-cancer-classifier python main.py
```

This will:
- Ingest and preprocess data
- Train the model
- Save the trained model to `artifacts/`

---

## 🔹 Evaluate the Model

```bash
docker run chest-cancer-classifier python src/cnnClassifier/pipeline/stage_04_model_evaluation.py
```

Evaluation results will be saved to `scores.json`.

---

## 🔹 Output Files

- `artifacts/` – Trained models and intermediate outputs
- `scores.json` – Evaluation results and performance metrics

---

## 🔹 Requirements

- Docker installed on your system
- Dataset placed in the correct folder structure
- Internet connection (for downloading pre-trained weights, if needed)

---

## 🔹 License

This project is licensed under the MIT License.



