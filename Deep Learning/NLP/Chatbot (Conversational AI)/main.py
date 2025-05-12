from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import logging
import os

# Load environment variables
load_dotenv()

os.makedirs("log", exist_ok=True)
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join("log", "app.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
logger.info(f"Static files mounted at /static from directory: {os.path.abspath('static')}")
templates = Jinja2Templates(directory="templates")

# Get Groq API key from environment
grok_api_key = os.getenv("GROK_API_KEY")
if not grok_api_key:
    logger.error("GROK_API_KEY not found in environment variables")
    raise HTTPException(status_code=500, detail="API key not configured")

try:
    chat = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.3, groq_api_key=grok_api_key)
    logger.info("ChatGroq model initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize ChatGroq: {str(e)}")
    raise HTTPException(status_code=500, detail="Failed to initialize chatbot model")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request, "messages": []})
    except Exception as e:
        logger.error(f"Error rendering chat page: {str(e)}")
        raise HTTPException(status_code=500, detail="Error loading chat interface")

@app.post("/chat")
async def post_chat(request: Request, message: str = Form(...)):
    try:
        response = chat.invoke(message).content
        logger.info(f"Successfully processed message: {message}")
        return {"message": response}
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail="Error generating response")

if __name__ == "__main__":
    try:
        import uvicorn
        logger.info("Starting FastAPI application")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")