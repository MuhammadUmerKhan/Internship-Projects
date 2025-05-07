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
    # API Keys (Keep them private using .env)
    GROQ_API_KEY = os.getenv("GROK_API_KEY")  # 🔑 Retrieves the Groq API key from environment variables
    logging.info("✅ API Key Found!")  # ✅ Logs a success message if the API key is found
except:
    logging.error("❌ API KEYS not found or not set.")  # ❌ Logs an error if the API key is missing

try:
    PROMPT_TEMPLATE_PATH = os.path.join("..", "prompt", "roman_urdu_prompt.txt")  # 📋 Sets the path to the prompt template file for Roman Urdu conversion
    logging.info("✅ Prompt Template Found!")  # ✅ Logs a success message if the path is set (though this doesn't verify file existence)
except FileNotFoundError as f:  # ⚠️ Catches FileNotFoundError if the prompt file path is invalid
    print(f"❌ {f.filename} not found")  # 🖥️ Prints an error message to the console if the file is not found
    logging.error(f"❌ {f.filename} not found")  # ❌ Logs the error to the log file

try:
    # Configure the LLM using your utility
    llm = utils.configure_llm(MODEL_NAME="qwen-qwq-32b")
except Exception as e:
    print(f"❌ {e}")  # 🖥️ Prints an error message to the console if the file is not found
    logging.error(f"❌ {e}")  # ❌ Logs the error to the log file