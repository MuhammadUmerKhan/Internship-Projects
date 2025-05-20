from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import joblib
import numpy as np
import os

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Prediction App",
    description="Predict diabetes risk using a trained Random Forest model.",
    version="1.0.0"
)

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Load Random Forest model
MODEL_PATH = os.path.join("scaler", "model.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file not found. Ensure 'models/rf_model.pkl' exists.")

model = joblib.load(MODEL_PATH)

# Feature names and constraints
FEATURES = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]
CONSTRAINTS = {
    "Pregnancies": {"min": 0, "max": 20, "type": "int"},
    "Glucose": {"min": 0, "max": 300, "type": "float"},
    "BloodPressure": {"min": 0, "max": 150, "type": "float"},
    "SkinThickness": {"min": 0, "max": 100, "type": "float"},
    "Insulin": {"min": 0, "max": 1000, "type": "float"},
    "BMI": {"min": 0, "max": 70, "type": "float"},
    "DiabetesPedigreeFunction": {"min": 0, "max": 3, "type": "float"},
    "Age": {"min": 0, "max": 120, "type": "int"}
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the homepage with the prediction form."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": None, "error": None}
    )

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pregnancies: float = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: float = Form(...)
):
    """Handle prediction requests and return results."""
    try:
        # Collect input data
        inputs = {
            "Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "BloodPressure": BloodPressure,
            "SkinThickness": SkinThickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
            "Age": Age
        }

        # Validate inputs
        for feature, value in inputs.items():
            constraints = CONSTRAINTS[feature]
            min_val = constraints["min"]
            max_val = constraints["max"]
            dtype = constraints["type"]

            # Check range
            if value < min_val or value > max_val:
                return templates.TemplateResponse(
                    "index.html",
                    {
                        "request": request,
                        "prediction": None,
                        "error": f"{feature} must be between {min_val} and {max_val}."
                    }
                )

            # Check integer type
            if dtype == "int" and not float(value).is_integer():
                return templates.TemplateResponse(
                    "index.html",
                    {
                        "request": request,
                        "prediction": None,
                        "error": f"{feature} must be an integer."
                    }
                )

        # Prepare input array
        input_data = np.array([[
            inputs["Pregnancies"], inputs["Glucose"], inputs["BloodPressure"],
            inputs["SkinThickness"], inputs["Insulin"], inputs["BMI"],
            inputs["DiabetesPedigreeFunction"], inputs["Age"]
        ]])

        # Make prediction
        prediction_proba = model.predict_proba(input_data)[0][1]  # Probability of Diabetic (class 1)
        prediction = "Diabetic" if prediction_proba > 0.5 else "Non-Diabetic"
        confidence = prediction_proba if prediction == "Diabetic" else 1 - prediction_proba

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": {
                    "result": prediction,
                    "confidence": f"{confidence:.2%}"
                },
                "error": None
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": None,
                "error": f"Prediction failed: {str(e)}"
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)