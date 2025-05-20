# Diabetes Prediction Notebooks

This `notebook` folder contains Jupyter notebooks and supporting code for the initial stages of a diabetes prediction project using the [Diabetes Dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set). The project aims to preprocess the dataset, explore data characteristics, train baseline machine learning models, and set the stage for further model development (e.g., deep neural networks). The workflow is designed for Google Colab, leveraging Python libraries and custom helper functions.

## Folder Structure
```
notebook/
├── 01_data_exploration.ipynb
├── 02_preprocessing_training.ipynb
├── helper/
│   └── helper.py
```

## Files Overview

### 1. `01_data_exploration.ipynb`
**Purpose**: Perform exploratory data analysis (EDA) on the Diabetes Dataset to understand its structure, distributions, and issues.

**Key Tasks**:
- **Load Data**: Reads the dataset (`diabetes.csv`) from `../data/raw/` (expected to be in `/content/drive/MyDrive/diabetes_project/data/raw/` in Colab).
- **Inspect Data**: Displays shape (768 rows, 9 columns: 8 features + `Outcome`), data types, and first few rows.
- **Analyze Distributions**: Generates histograms for features (e.g., `Glucose`, `BMI`) and a class distribution plot for `Outcome` (~65% non-diabetic, ~35% diabetic).
- **Identify Issues**: Detects zeros in `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` (~35% zeros in `Insulin`, ~30% in `SkinThickness`), indicating implicit missing values.
- **Visualize Correlations**: Creates a correlation heatmap to identify relationships (e.g., `Glucose` and `Outcome` correlation).
- **Save Outputs**: Saves plots to `../plots/` (e.g., `class_distribution.png`, `correlation_heatmap.png`) and an outlier summary to `../results/outliers_summary.csv`.

**Outputs**:
- Plots in `../plots/` for distributions and correlations.
- Outlier summary in `../results/`.
- Insights for preprocessing (e.g., handle zeros, address class imbalance).

**Dependencies**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `os`.

### 2. `02_preprocessing_training.ipynb`
**Purpose**: Preprocess the dataset and train baseline machine learning models to establish initial performance metrics.

**Key Tasks**:
- **Load Data**: Reads `diabetes.csv` from `../data/`.
- **Handle Zeros**: Replaces zeros in `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` with column medians to address implicit missing values.
- **Split Data**: Splits data into features (`X`: 8 features) and target (`y`: `Outcome`), then performs a stratified train-test split (80% train, 20% test).
- **Balance Classes**: Applies SMOTEENN (SMOTE + Edited Nearest Neighbors) to the training set to address class imbalance, producing a balanced `X_resampled_enn` and `y_resampled_enn` (~400–600 rows, ~50:50 classes).
- **Train Models**: Trains three models using resampled data:
  - Random Forest (`RandomForestClassifier`, saved as `rf_model.pkl`).
  - K-Nearest Neighbors (`KNeighborsClassifier`, k=5).
  - Support Vector Machine (`SVC`, RBF kernel).
- **Evaluate Models**: Uses `evaluate_model` (from `helper.py`) to compute ROC curves (FPR, TPR, AUC) and accuracy, with scaling for KNN and SVM.
- **Visualize Results**: Calls `plot_model_comparisons` (from `helper.py`) to generate ROC curve plots, saved to `../plots/` (e.g., `model_comparisons.png`).
- **Save Outputs**: Saves the Random Forest model to `../models/rf_model.pkl`.

**Outputs**:
- Preprocessed training data (balanced with SMOTEENN).
- Trained Random Forest model in `../models/`.
- Comparison plots in `../plots/`.
- Expected ROC-AUC: ~0.80–0.85 for Random Forest, ~0.75–0.80 for KNN/SVM.

**Dependencies**: `pandas`, `numpy`, `os`, `sklearn`, `imblearn`, `helper.helper`.

### 3. `helper/helper.py`
**Purpose**: Provide reusable functions for model evaluation and visualization, used by `02_preprocessing_training.ipynb`.

**Key Functions**:
- **`evaluate_model(model, X, y, need_scaling=False, save=False)`**:
  - Scales data if `need_scaling=True` (for KNN, SVM) using `StandardScaler`.
  - Trains the model on `X` and `y`.
  - Computes ROC metrics (FPR, TPR, AUC) and accuracy, likely via cross-validation or test set.
  - Saves the model (e.g., `rf_model.pkl`) if `save=True`.
  - Returns `fpr`, `tpr`, `roc_auc`, `acc`.
- **`plot_model_comparisons(results)`**:
  - Takes a dictionary of model results (`{name: (fpr, tpr, roc_auc, acc)}`).
  - Generates ROC curve plots for each model.
  - May include accuracy bar plots or other metrics.
  - Saves plots to `../plots/` (e.g., `model_comparisons.png`).

**Role**: Modularizes evaluation and visualization logic, ensuring consistency and reusability.

**Dependencies**: Likely `sklearn`, `matplotlib`, `joblib` (exact dependencies depend on implementation).

## Project Workflow
The notebooks represent the initial stages of a diabetes prediction pipeline:
1. **EDA (`01_data_exploration.ipynb`)**:
   - Understands dataset characteristics (768 rows, 9 columns).
   - Identifies issues: zeros (~35% in `Insulin`), class imbalance (~65:35).
   - Saves visualizations and summaries to guide preprocessing.
2. **Preprocessing & Baseline Training (`02_preprocessing_training.ipynb`)**:
   - Addresses zeros with median imputation.
   - Balances classes with SMOTEENN.
   - Trains and evaluates baseline models (Random Forest, KNN, SVM).
   - Saves the Random Forest model and comparison plots.
3. **Helper Functions (`helper.py`)**:
   - Supports model evaluation and visualization in `02_preprocessing_training.ipynb`.
   - Enables scalable code reuse for future notebooks (e.g., DNN training).

**Next Steps** (Not Implemented):
- **Model Tuning**: Hyperparameter tuning for Random Forest or other models (e.g., in a `03_model_training.ipynb`).
- **Deep Learning**: Train a deep neural network (DNN) using TensorFlow/Keras.
- **Web App**: Deploy the model in a FastAPI web app for user-friendly predictions (already implemented separately).

## Setup Instructions
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd diabetes_project
   ```
2. **Set Up Environment**:
   - Install dependencies in a virtual environment or Colab:
     ```bash
     pip install pandas numpy matplotlib seaborn scikit-learn imblearn
     ```
   - In Colab:
     ```python
     !pip install pandas numpy matplotlib seaborn scikit-learn imblearn
     ```
3. **Prepare Data**:
   - Download `diabetes.csv` from [Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set).
   - Place it in `../data/raw/` (e.g., `/content/drive/MyDrive/diabetes_project/data/raw/` in Colab).
4. **Mount Google Drive** (for Colab):
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
5. **Run Notebooks**:
   - Open `01_data_exploration.ipynb` in Colab or Jupyter.
   - Execute cells sequentially to generate plots and summaries.
   - Run `02_preprocessing_training.ipynb` to preprocess data, train models, and save outputs.
6. **Verify Outputs**:
   - Check `../plots/` for visualizations (e.g., `class_distribution.png`, `model_comparisons.png`).
   - Confirm `../models/rf_model.pkl` and `../results/outliers_summary.csv` exist.

## Assumptions
- **Environment**: Notebooks are designed for Google Colab with Google Drive mounted.
- **Data Path**: `diabetes.csv` is in `../data/raw/` relative to the notebook folder (e.g., `/content/drive/MyDrive/diabetes_project/data/raw/`).
- **Helper Functions**: `helper.py` is correctly implemented and accessible via `from helper.helper import evaluate_model, plot_model_comparisons`.
- **Dependencies**: All required libraries are installed (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `imblearn`).
- **Model Saving**: `evaluate_model` in `helper.py` saves models to `../models/` and plots to `../plots/`.

## Project Structure (Context)
The `notebook` folder is part of a larger project:
```
/content/drive/MyDrive/diabetes_project/
├── data/
│   |── diabetes.csv
├── models/
│   └── rf_model.pkl
├── notebook/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing_training.ipynb
│   ├── helper/
│   │   └── helper.py
├── templates/
│   └── index.html
├── app.py
```

## Notes
- **Execution Time**: 
  - `01_data_exploration.ipynb`: ~30–60 seconds (EDA, plotting).
  - `02_preprocessing_training.ipynb`: ~1–2 minutes (preprocessing, model training).
- **Colab Path**: Update paths in notebooks if not using `/content/drive/MyDrive/diabetes_project/` (e.g., set `raw_data_path = "/content/drive/MyDrive/your_path/data/raw"`).
- **Helper Dependency**: Without `helper.py` content, I assume `evaluate_model` and `plot_model_comparisons` handle scaling, evaluation, and plotting. Share `helper.py` for precise documentation.
- **Outputs**: Ensure write permissions for `../plots/`, `../models/`, and `../results/` in Colab.
- **Next Notebook**: A `03_model_training.ipynb` could tune models or train a DNN, using outputs from `02_preprocessing_training.ipynb`.

## Troubleshooting
- **FileNotFoundError**: If `diabetes.csv` is missing, download it and place it in `../data/raw/`. Verify paths in notebooks.
- **Import Error**: Ensure `helper.py` is in `notebook/helper/` and dependencies are installed.
- **Plotting Issues**: Check `../plots/` permissions. In Colab, use `%matplotlib inline`.
- **Model Saving**: Confirm `evaluate_model` saves `rf_model.pkl` to `../models/`.

## Next Steps
- **Share Helper Code**: Provide `helper.py` for detailed function descriptions.
- **Run Notebooks**: Execute `01_data_exploration.ipynb` and `02_preprocessing_training.ipynb` to generate outputs.
- **Extend Workflow**: Request a `03_model_training.ipynb` for DNN training or hyperparameter tuning.
- **Feedback**: Report errors (e.g., path issues, import failures) with logs or screenshots for troubleshooting.
- **Web App**: Continue using the FastAPI app (`app.py`, `index.html`) for predictions, leveraging `rf_model.pkl`.

For questions or assistance, contact the project maintainer or share details via the repository’s issue tracker.