# Diabetes Prediction Project 🩺

Welcome to the Diabetes Prediction Project! This repository builds a machine learning pipeline to predict diabetes risk using the [Diabetes Dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) 📊. The project includes data exploration, preprocessing, model training, and a user-friendly FastAPI web app for real-time predictions. It’s designed for Google Colab with Google Drive integration but can be adapted for local setups.

---

## Project Overview 🌟
- **Objective**: Predict diabetes risk (`Outcome`: 0 = Non-Diabetic, 1 = Diabetic) using features like `Glucose`, `BMI`, and `Age`.
- **Dataset**: Diabetes Dataset (768 rows, 9 columns: 8 features + `Outcome`).
- **Workflow**:
  1. Explore data to identify issues (e.g., zeros, class imbalance) 📈.
  2. Preprocess data and train baseline models (Random Forest, KNN, SVM) 🤖.
  3. Deploy a web app for predictions using the trained Random Forest model 🌐.
- **Key Outputs**:
  - Trained Random Forest model (`model.pkl`, ROC-AUC ~80–85%) ✅.
  - FastAPI web app with a dark-themed, diabetes-focused UI 🩺.

---

## Project Structure 🗂️
```
diabetes_project/
├── data/
│   └── diabetes.csv
├── models/
│   └── model.pkl
|   └── scaler.pkl
│
├── notebook/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing_training.ipynb
│   ├── helper/
│   │   └── helper.py
│   └── README.md
│
├── templates/
│   └── index.html
│
└── app.py
```

---

### Key Components
- **`data/`** 📂:
  - `diabetes.csv`: Raw dataset (768 rows, 9 columns).
- **`models/`** 🤖:
  - `model.pkl`: Trained Random Forest model for predictions.
- **`notebook/`** 📓:
  - `01_data_exploration.ipynb`: EDA (distributions, correlations, zeros ~35% in `Insulin`).
  - `02_preprocessing_training.ipynb`: Preprocessing (impute zeros, balance classes) and training (Random Forest, KNN, SVM).
  - `helper/helper.py`: Functions for model evaluation (`evaluate_model`) and plotting (`plot_model_comparisons`).
  - `README.md`: Notebook-specific documentation.
- **`templates/`** 🌐:
  - `index.html`: Web app UI (dark theme, two-column inputs, emojis 🩺, animations, “Diabetes Facts” section).
- **`app.py`** 🚀:
  - FastAPI script to load `model.pkl`, serve the web app, and handle predictions.

## Workflow 🔄
1. **Data Exploration** (`01_data_exploration.ipynb`) 📈:
   - Loads `diabetes.csv`, analyzes distributions (~65% non-diabetic), identifies zeros (~30% in `SkinThickness`).
   - Saves plots to `plots/` and summaries to `results/`.
2. **Preprocessing & Training** (`02_preprocessing_training.ipynb`) 🤖:
   - Imputes zeros with medians, splits data (80% train, 20% test), balances training data with SMOTEENN.
   - Trains Random Forest (saved as `model.pkl`), KNN, and SVM.
   - Evaluates models (Random Forest AUC ~0.80–0.85) and saves plots.
3. **Web App Deployment** (`app.py`, `index.html`) 🌐:
   - Loads `model.pkl`, serves a dark-themed UI with two-column inputs (4 rows, 2 inputs each).
   - Validates inputs (e.g., `Glucose` 0–300), displays predictions with confidence (e.g., “Low Diabetes Risk ✅, 82.50%”).

## Setup Instructions ⚙️
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd diabetes_project
   ```
2. **Install Dependencies**:
   - Locally:
     ```bash
     pip install pandas numpy matplotlib seaborn scikit-learn imblearn fastapi uvicorn jinja2
     ```
   - In Colab:
     ```bash
     !pip install pandas numpy matplotlib seaborn scikit-learn imblearn fastapi uvicorn jinja2 nest-asyncio
     ```
3. **Prepare Data** 📥:
   - Download `diabetes.csv` from [Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set).
   - Place it in `data/raw/` (e.g., `/content/drive/MyDrive/diabetes_project/data/raw/`).
4. **Mount Google Drive** (Colab):
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
5. **Run Notebooks** 📓:
   - Open `notebook/01_data_exploration.ipynb` and execute cells to generate plots and summaries.
   - Run `notebook/02_preprocessing_training.ipynb` to preprocess data, train models, and save `model.pkl`.
6. **Launch Web App** 🌐:
   - Locally:
     ```bash
     python app.py
     ```
     Open `http://localhost:8000`.
   - In Colab:
     ```python
     import nest_asyncio
     import uvicorn
     nest_asyncio.apply()
     uvicorn.run(app, host="0.0.0.0", port=8000)
     ```

## Usage 🩺
1. **Explore Data**:
   - Run `01_data_exploration.ipynb` to view distributions and correlations 📊.
2. **Train Models**:
   - Execute `02_preprocessing_training.ipynb` to preprocess data and train models 🤖.
   - Verify `model.pkl` in `models/`.
3. **Use Web App**:
   - Launch `app.py`, open `http://localhost:8000` (or `ngrok` URL in Colab) 🌐.
   - Enter health metrics (e.g., `Glucose: 120`, `BMI: 30`) in the two-column form.
   - Click **Analyze Risk 🚀** to see predictions (e.g., “Low Diabetes Risk ✅, Confidence: 82.50%”).
   - Explore the “Diabetes Facts” section for insights 🩺.

## Key Features ✨
- **Data Exploration**: Identifies zeros (~35% in `Insulin`) and class imbalance (~65:35) 📈.
- **Preprocessing**: Imputes zeros, balances classes with SMOTEENN ⚖️.
- **Models**: Random Forest (AUC ~0.80–0.85), KNN, SVM 🤖.
- **Web App**:
  - Dark theme (navy gradient `#1a1a2e` to `#16213e`) 🌙.
  - Two-column input layout (4 rows, 2 inputs each) 📝.
  - Emojis (🩺, 💉, ✅) and animations (fade-in, spinner, slide-in) 🎉.
  - Input validation (e.g., `Pregnancies` 0–20, integers) ✅.
  - “Diabetes Facts” section and footer links (Privacy, Help, About) ℹ️.

## Assumptions 📋
- **Environment**: Google Colab with Google Drive at `/content/drive/MyDrive/diabetes_project/`.
- **Dependencies**: All libraries installed (`pandas`, `scikit-learn`, `fastapi`, etc.).
- **Data Path**: `diabetes.csv` in `data/raw/`.
- **Helper Functions**: `helper.py` provides `evaluate_model` and `plot_model_comparisons`.
- **Permissions**: Write access to `plots/`, `models/`, and `results/` in Colab.

## Troubleshooting 🔧
- **FileNotFoundError**: Ensure `diabetes.csv` is in `data/raw/` and `model.pkl` in `models/`.
- **Import Error**: Verify `helper.py` in `notebook/helper/` and dependencies installed.
- **Plotting Issues**: Use `%matplotlib inline` in Colab; check `plots/` permissions.
- **Web App Fails**: Confirm `app.py` loads `model.pkl`; check port `8000` availability.
- **Colab Access**: Use `ngrok` for public URL if running in Colab.

## Next Steps 🚀
- **Run Pipeline**: Execute notebooks and launch the web app to test predictions 🩺.
- **Extend Models**: Add a `notebook/03_model_training.ipynb` for DNN training or hyperparameter tuning 🤖.
- **Enhance Web App**: Add features like prediction history or feature importance display 🌐.
- **Production Deployment**: Deploy on Heroku or a similar platform for public access ☁️.
- **Share Feedback**: Report issues (e.g., path errors, UI bugs) with logs or screenshots 📬.

## Contact 📧
For support, share details via the repository’s issue tracker or contact the project maintainer. Let’s make diabetes prediction accessible and impactful! 🌟