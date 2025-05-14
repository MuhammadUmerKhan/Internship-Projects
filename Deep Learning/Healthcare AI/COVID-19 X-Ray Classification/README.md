# 🩺 COVID-19 X-Ray Classification Project

This project, **COVID-19-XRAY-CLASSIFICATION**, focuses on classifying chest X-ray images to diagnose COVID-19 and related conditions using a deep learning model (ResNet-50). It includes data exploration, preprocessing, model training, and a web application for real-time predictions. The project leverages PyTorch for model training and FastAPI for the web app, providing a professional interface to upload X-ray images and obtain predictions with probabilities.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Running the Notebooks](#running-the-notebooks)
  - [Running the Web Application](#running-the-web-application)
- [Outputs](#outputs)
- [Technical Details](#technical-details)
- [Notes and Recommendations](#notes-and-recommendations)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

## 🌟 Project Overview

The goal of this project is to build and deploy a deep learning model for classifying chest X-ray images into four categories: `COVID`, `Normal`, `Viral Pneumonia`, and `Lung_Opacity`. The project is divided into two main phases:
1. **Data Analysis and Model Training**: Uses Jupyter notebooks to explore the dataset, preprocess images, train a ResNet-50 model, and evaluate its performance.
2. **Web Application Deployment**: Deploys the trained model using FastAPI, allowing users to upload X-ray images and get predictions through a professional web interface.

The project uses the **COVID-19 Radiography Dataset** from Kaggle, a pre-trained ResNet-50 model fine-tuned for the task, and a FastAPI web app with a sleek, dark-themed UI.

## ✨ Features

- **Data Exploration**: Visualizes sample images and class distributions to understand dataset balance.
- **Stratified Splitting**: Splits the dataset into training (70%), validation (15%), and test (15%) sets while maintaining class proportions.
- **Data Preprocessing**: Applies image transformations (resize, augmentation, normalization) for ResNet-50 compatibility.
- **Model Training**: Fine-tunes a pre-trained ResNet-50 model for 4-class classification.
- **Evaluation**: Provides accuracy, confusion matrix, and classification report for model performance.
- **Web Application**: A user-friendly interface to upload X-ray images and receive predictions with probabilities.
- **Professional UI**: Dark-themed, responsive design with inline CSS and JavaScript for a seamless experience.

## 📁 Project Structure

```
COVID-19-XRAY-CLASSIFICATION/
│
├── 📂 assets/                          # Directory for static assets (e.g., images, styles)
│   └── (empty or contains assets like logos, figures, etc.)
│
├── 📂 data/                            # Directory for dataset storage
│   └── (contains the COVID-19 Radiography Dataset, e.g., COVID_Dataset/)
│       └── 📂 COVID_Dataset/           # Structured dataset with class subfolders
│           ├── 📂 COVID/               # Images for COVID class
│           ├── 📂 Normal/              # Images for Normal class
│           ├── 📂 Viral Pneumonia/     # Images for Viral Pneumonia class
│           └── 📂 Lung_Opacity/        # Images for Lung Opacity class
│
├── 📂 models/                          # Directory for trained model weights
│   └── 📄 resnet50_covid_classifier.pth  # Trained ResNet-50 model weights
│
├── 📂 notebook/                        # Directory for Jupyter notebooks
│   ├── 📓 01_data_exploration.ipynb    # Notebook for dataset exploration and visualization
│   └── 📓 02_preprocessing_&_training.ipynb  # Notebook for preprocessing, training, and evaluation

├── 📂 template/
│   └── 📄 index.html                    # HTML template file
│
├── 📄 main.py                          # FastAPI backend
|
├── 📜 README.md                        # Main project README with instructions
│
├── 📜 gitignore.md                     # Gitignore file (likely a typo, should be .gitignore)
│
└── 📜 requirements.txt                 # File listing project dependencies
```

### File and Directory Descriptions:
- **`assets/`**: Placeholder for static assets (e.g., images for documentation).
- **`data/COVID_Dataset/`**: Contains the dataset with class-specific subfolders.
- **`models/resnet50_covid_classifier.pth`**: Saved weights of the trained ResNet-50 model.
- **`notebook/`**:
  - `01_data_exploration.ipynb`: Explores the dataset, visualizes sample images, and plots class distribution.
  - `02_preprocessing_&_training.ipynb`: Handles preprocessing, training, and evaluation of the model.
- **`templates/index.html`**: Frontend for the web app with inline CSS and JavaScript.
- **`main.py`**: FastAPI backend to serve the web app and handle predictions.
- **`README.md`**: Comprehensive project documentation.
- **`gitignore.md`**: Likely intended as `.gitignore` to exclude large files from Git.
- **`requirements.txt`**: Lists Python dependencies.

## 📂 Dataset

The project uses the **COVID-19 Radiography Dataset** from Kaggle, which contains chest X-ray images categorized into four classes:
- `COVID`
- `Normal`
- `Viral Pneumonia`
- `Lung_Opacity`

**Source**: [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

**Structure**:
```
data/COVID_Dataset/
├── COVID/
├── Normal/
├── Viral Pneumonia/
├── Lung_Opacity/
```

**Setup**:
1. Download the dataset from Kaggle.
2. Extract and place it in `data/COVID_Dataset/` with the structure above.

## 🛠️ Prerequisites

- **Python**: Version 3.8+ (tested with 3.12).
- **Hardware**: CPU (GPU optional; model loading is configured for CPU).
- **Dependencies**:
  - `torch`: For model loading and inference.
  - `torchvision`: For ResNet-50 and image transforms.
  - `fastapi`: For the web application backend.
  - `uvicorn`: ASGI server to run FastAPI.
  - `jinja2`: For rendering HTML templates.
  - `pillow`: For image processing.
  - Additional libraries for notebooks: `matplotlib`, `seaborn`, `pandas`, `scikit-learn`, `jupyter`.

## 📦 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd COVID-19-XRAY-CLASSIFICATION
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required packages:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

   **Sample `requirements.txt`**:
   ```
   torch==2.0.1
   torchvision==0.15.2
   fastapi==0.111.0
   uvicorn==0.29.0
   jinja2==3.1.3
   pillow==10.3.0
   matplotlib==3.8.4
   seaborn==0.13.2
   pandas==2.2.2
   scikit-learn==1.4.2
   jupyter==1.0.0
   ```

3. **Prepare Dataset**:
   - Download the dataset from Kaggle.
   - Extract and place it in `data/COVID_Dataset/` as shown above.

4. **Verify Model File**:
   - Ensure `models/resnet50_covid_classifier.pth` exists. This file is generated by running `02_preprocessing_&_training.ipynb`.

## 🚀 Usage

### Running the Notebooks

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Run `01_data_exploration.ipynb`**:
   - Open `notebook/01_data_exploration.ipynb`.
   - Execute cells to visualize sample images and class distribution.
   - Output: `class_distribution.png`.

3. **Run `02_preprocessing_&_training.ipynb`**:
   - Open `notebook/02_preprocessing_&_training.ipynb`.
   - Execute cells to preprocess data, train the model, and evaluate performance.
   - Outputs: `class_distribution.png`, `confusion_matrix.png`, `models/resnet50_covid_classifier.pth`.

### Running the Web Application

1. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Web App**:
   - Open your browser and go to `http://127.0.0.1:8000`.
   - Upload an X-ray image (JPEG/PNG) and click "Predict" to see the classification result with probability (e.g., "The image is classified as COVID with a probability of 0.95 (95%)").

## 📈 Outputs

### From Notebooks:
- **Images**:
  - `class_distribution.png`: Bar plot of class distribution (from both notebooks).
  - `confusion_matrix.png`: Heatmap of test set predictions (from `02_preprocessing_&_training.ipynb`).
- **Model**:
  - `models/resnet50_covid_classifier.pth`: Trained ResNet-50 weights.
- **Console**:
  - Dataset statistics, training logs, test accuracy, and classification metrics.

### From Web Application:
- **Web Interface**: Displays the predicted class and probability for an uploaded X-ray image.
- **JSON Response** (via `/predict` endpoint):
  ```json
  {
    "predicted_class": "COVID",
    "probability": 0.9473,
    "message": "The image is classified as COVID with a probability of 0.95"
  }
  ```

## 🛠️ Technical Details

- **Model**: Pre-trained ResNet-50, fine-tuned for 4-class classification (`COVID`, `Normal`, `Viral Pneumonia`, `Lung_Opacity`).
- **Training**:
  - Dataset split: 70% training, 15% validation, 15% test (stratified).
  - Preprocessing: Resize to 224x224, random rotation (±10°), horizontal flip (50%), ImageNet normalization.
  - Optimizer: Adam with learning rate 0.0001.
  - Loss: CrossEntropyLoss.
  - Epochs: 10 (configurable in `02_preprocessing_&_training.ipynb`).
- **Web App**:
  - Backend: FastAPI with Jinja2 for templating.
  - Frontend: Single `index.html` with inline CSS (dark theme, responsive) and JavaScript (fetch API for predictions).
  - Endpoint: `/predict` (POST) for uploading images and receiving predictions.
- **Inference**:
  - Model loaded on CPU (configured with `map_location='cpu'` due to CUDA unavailability).
  - Image preprocessing matches training (resize, normalize).

## ⚠️ Notes and Recommendations

- **Hardware**:
  - Currently configured for CPU inference. For GPU support, remove `map_location` and ensure CUDA is available.
  - Adjust `batch_size` in `02_preprocessing_&_training.ipynb` (default: 128) if memory issues occur.
- **Dataset**:
  - The dataset may be imbalanced (e.g., more `Normal` images). Consider class weights in the loss function for better minority class performance.
  - Ensure images are in JPEG/PNG format for compatibility with PIL.
- **Web App**:
  - The UI is minimal but professional. Enhance with additional features (e.g., image preview, multiple uploads) if needed.
  - For production, add security measures (e.g., file size limits, input validation, HTTPS).
- **Notebooks**:
  - Set `num_workers=0` in DataLoaders on Windows if multiprocessing issues arise.
  - Increase `num_epochs` (e.g., to 20) or add early stopping for better model performance.
- **gitignore.md**: Likely a typo; rename to `.gitignore` to exclude large files (e.g., dataset, model weights) from Git.

## 🐛 Troubleshooting

- **Model Loading Error**:
  - **Issue**: "Cannot deserialize object on CUDA device."
  - **Solution**: Ensure `map_location=torch.device('cpu')` is used in `main.py` if no GPU is available.
- **File Not Found**:
  - **Issue**: `models/resnet50_covid_classifier.pth` not found.
  - **Solution**: Run `02_preprocessing_&_training.ipynb` to generate the model file, or verify the path.
- **Image Upload Fails**:
  - **Issue**: Prediction endpoint returns an error.
  - **Solution**: Ensure the uploaded image is a valid JPEG/PNG and matches the expected preprocessing (e.g., RGB format).
- **Dependency Issues**:
  - **Issue**: Missing libraries.
  - **Solution**: Install all dependencies listed in `requirements.txt`.

## 📬 Contact

For questions, issues, or contributions, contact the project maintainer or refer to the dataset documentation on Kaggle.

**Last Updated**: 11:01 PM PKT, Wednesday, May 14, 2025.

Happy classifying! 🎉