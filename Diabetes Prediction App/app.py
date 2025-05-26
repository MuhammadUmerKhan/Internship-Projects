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
    description="Predict diabetes risk using a trained SVC model.",
    version="1.0.0"
)

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Load SVC model and scaler
MODEL_PATH = os.path.join("scaler", "model_SVC.pkl")
SCALER_PATH = os.path.join("scaler", "scaler_SVC.pkl")

if not (os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH)):
    raise FileNotFoundError("Model or scaler file not found. Ensure 'scaler/model_SVC.pkl' and 'scaler/scaler_SVC.pkl' exist.")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Feature names and constraints (excluding Glucose)
FEATURES = [
    "Pregnancies", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]
CONSTRAINTS = {
    "Pregnancies": {"min": 0, "max": 20, "type": "int"},
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

        # Prepare input array (excluding Glucose)
        input_data = np.array([[
            inputs["Pregnancies"], inputs["BloodPressure"], inputs["SkinThickness"],
            inputs["Insulin"], inputs["BMI"], inputs["DiabetesPedigreeFunction"], inputs["Age"]
        ]])

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make prediction with SVC
        prediction_proba = model.predict_proba(input_data_scaled)[0][1]  # Probability of Diabetic (class 1)
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