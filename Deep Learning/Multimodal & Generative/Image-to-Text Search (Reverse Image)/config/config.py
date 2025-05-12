import os, logging  # 📥 Import os for file path operations and logging for logging functionality
from dotenv import load_dotenv  # 📥 Import load_dotenv to load environment variables from a .env file
from utils import utils  # 📥 Import utils module configuration

# Load environment variables from .env file
load_dotenv()  # 🔄 Loads environment variables from .env file into the application

# Logging configuration
os.makedirs(os.path.join("logs"), exist_ok=True)  # 📂 Creates a 'logs' directory if it doesn't exist
logging.basicConfig(  # ⚙️ Configures the logging system with specified settings
    level=logging.INFO,  # 📏 Sets logging level to INFO to capture informational messages and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # 📝 Defines log message format: timestamp, level, and message
    handlers=[  # 📤 Specifies where logs are sent
        logging.FileHandler(os.path.join("logs", "logging.log")),  # 📜 Logs to a file named 'logging.log' in the 'logs' directory
        logging.StreamHandler()  # 🖥️ Also logs to the console (standard output)
    ]
)

try:
    
    GROQ_API_KEY = os.getenv("GROK_API_KEY")  
    logging.info("✅ API Key Found!")  
except:
    logging.error("❌ API KEYS not found or not set.")  

try:
    # Configure the LLM using your utility
    llm = utils.configure_llm(MODEL_NAME="qwen-qwq-32b")
except Exception as e:
    print(f"❌ {e}")  # 🖥️ Prints an error message to the console if the file is not found
    logging.error(f"❌ {e}")  # ❌ Logs the error to the log file