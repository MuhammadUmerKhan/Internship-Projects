# 📚 Notebook Folder: COVID-19 Radiography Dataset Analysis

This folder, `notebook`, contains two Jupyter notebooks for analyzing and modeling the **COVID-19 Radiography Dataset**. The notebooks cover data exploration, preprocessing, model training, and evaluation using PyTorch and ResNet-50 for classifying chest X-ray images into categories like `COVID`, `Normal`, `Viral Pneumonia`, and `Lung_Opacity`.

## 📋 Table of Contents
- [Overview](#overview)
- [Notebooks](#notebooks)
  - [01_data_exploration.ipynb](#01_data_explorationipynb)
  - [02_preprocessing_&_training.ipynb](#02_preprocessing__trainingipynb)
- [Dataset](#dataset)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Outputs](#outputs)
- [Notes](#notes)
- [Contact](#contact)

## 🌟 Overview

The notebooks in this folder are part of a project to build a deep learning model for classifying chest X-ray images from the COVID-19 Radiography Dataset. They demonstrate:
- **Data Exploration**: Visualizing sample images and class distributions.
- **Preprocessing**: Structuring the dataset, applying data augmentation, and splitting into training/validation/test sets.
- **Model Training**: Fine-tuning a pre-trained ResNet-50 model.
- **Evaluation**: Assessing model performance with accuracy, confusion matrix, and classification report.

## 📓 Notebooks

### 1. `01_data_exploration.ipynb`

**Purpose**: Explores the COVID-19 Radiography Dataset to understand its structure and class distribution.

**Key Tasks**:
- 📁 Lists class folders (e.g., `COVID`, `Normal`, `Viral Pneumonia`, `Lung_Opacity`).
- 🖼️ Visualizes sample images from each class in grayscale.
- 📊 Plots a bar chart of class distribution in a dark theme to identify imbalances.
- 🔢 Computes and May contain errors due to the use of deprecated or non-standard methods, functions, or classes.

**Outputs**:
- Console output: List of classes and sample image paths.
- Image: `class_distribution.png` (bar plot of class counts).

### 2. `02_preprocessing_&_training.ipynb`

**Purpose**: Preprocesses the dataset, trains a ResNet-50 model, and evaluates its performance.

**Key Tasks**:
- 🗂️ Loads the dataset from `dataset/COVID_Dataset/` using `ImageFolder`.
- ✂️ Performs stratified splitting (70% training, 15% validation, 15% test).
- 🔧 Applies preprocessing transforms (resize to 224x224, random rotation, horizontal flip, normalization).
- 📦 Creates `DataLoader` objects for efficient batch processing.
- 📊 Visualizes class distribution across splits in a dark-themed bar plot.
- 🧠 Fine-tunes a pre-trained ResNet-50 model with a modified final layer (4 classes).
- 🚀 Trains the model for 10 epochs using Adam optimizer and CrossEntropyLoss.
- 🔍 Evaluates test set performance (accuracy, confusion matrix, classification report).
- 💾 Saves the trained model weights.

**Outputs**:
- Console output: Dataset details, training progress, test accuracy, classification report.
- Images: `class_distribution.png`, `confusion_matrix.png`.
- Model: `models/resnet50_covid_classifier.pth`.

## 📂 Dataset

The notebooks assume the COVID-19 Radiography Dataset is available in `dataset/COVID_Dataset/` with the following structure:
```
dataset/COVID_Dataset/
├── COVID/
├── Normal/
├── Viral Pneumonia/
├── Lung_Opacity/
```

**Source**: [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) on Kaggle.

**Setup**:
1. Download the dataset from Kaggle.
2. Extract it to `dataset/`.
3. Organize images into class-specific subfolders as shown above.

## 🛠️ Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install torch torchvision matplotlib seaborn pandas scikit-learn pillow jupyter
   ```
2. **Prepare Dataset**:
   - Ensure `dataset/COVID_Dataset/` is correctly structured.
   - Update `DATASET_DIR` in `02_preprocessing_&_training.ipynb` if the path differs.
3. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   Open the notebooks from the Jupyter interface.

## 🚀 Usage

1. **Run `01_data_exploration.ipynb`**:
   - Execute cells sequentially to explore the dataset.
   - Check `class_distribution.png` for class balance insights.
2. **Run `02_preprocessing_&_training.ipynb`**:
   - Execute cells to preprocess data, train the model, and evaluate performance.
   - Monitor training progress in the console.
   - Review `class_distribution.png`, `confusion_matrix.png`, and the classification report.
   - Use the saved model (`resnet50_covid_classifier.pth`) for inference.

## 📈 Outputs

- **Images**:
  - `class_distribution.png`: Bar plot of class distribution (both notebooks).
  - `confusion_matrix.png`: Heatmap of test set predictions (from `02_preprocessing_&_training.ipynb`).
- **Model**:
  - `models/resnet50_covid_classifier.pth`: Trained ResNet-50 weights.
- **Console**:
  - Dataset statistics, training logs, test accuracy, and classification metrics.

## ⚠️ Notes

- **Hardware**: A GPU is recommended for faster training. The script falls back to CPU if no GPU is available.
- **Batch Size**: Set to 128 in `02_preprocessing_&_training.ipynb`. Reduce to 64 or 32 if GPU memory is limited.
- **Workers**: Uses 4 workers for data loading. Set `num_workers=0` on Windows if issues occur.
- **Imbalanced Data**: The dataset may have uneven class sizes (e.g., more `Normal` images). Consider class weights in the loss function for better minority class performance.
- **Epochs**: Training runs for 10 epochs. Increase to 20 or add early stopping for improved results.