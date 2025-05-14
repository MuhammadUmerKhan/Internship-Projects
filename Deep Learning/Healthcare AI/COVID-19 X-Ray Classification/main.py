import torch
import torchvision.transforms as transforms
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import torchvision.models as models
import torch.nn as nn
from PIL import Image
import io

app = FastAPI()

# Load the pre-trained ResNet-50 model with CPU mapping if no GPU is available
model = models.resnet50(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 4)  # 4 classes: COVID, Normal, Viral Pneumonia, Lung_Opacity
model.load_state_dict(torch.load("models/resnet50_covid_classifier.pth", map_location=torch.device('cpu')))
model.eval()
device = torch.device("cpu")  # Force CPU device since CUDA is unavailable
model = model.to(device)

# Define the same transforms used during training
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Class names
class_names = ["COVID", "Normal", "Viral Pneumonia", "Lung_Opacity"]

# Prediction function
def predict_image(image):
    # Convert uploaded image to PIL and apply transforms
    input_image = Image.open(io.BytesIO(image)).convert("RGB")
    input_tensor = transform(input_image).unsqueeze(0).to(device)
    
    # Get prediction
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        prob = probabilities[0][predicted_class].item()
    
    return class_names[predicted_class], prob

# Set up Jinja2 templates
templates = Jinja2Templates(directory="template")

# Serve the HTML template
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    predicted_class, probability = predict_image(contents)
    return {
        "predicted_class": predicted_class,
        "probability": probability,
        "message": f"The image is classified as {predicted_class} with a probability of {probability:.2f}"
    }