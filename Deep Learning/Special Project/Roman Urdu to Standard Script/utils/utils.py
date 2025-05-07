import os, logging  # 📥 Import os for file path operations and logging for logging functionality
from langchain_groq import ChatGroq  # 📥 Import ChatGroq for interacting with Groq API's LLM
from config import config as CONFIG  # 📥 Import config module (as CONFIG) for accessing API keys and settings

os.makedirs(os.path.join("logs"), exist_ok=True)  # 📂 Creates a 'logs' directory if it doesn't exist
logging.basicConfig(  # ⚙️ Configures the logging system with specified settings
    level=logging.INFO,  # 📏 Sets logging level to INFO for informational messages and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # 📝 Defines log message format: timestamp, level, and message
    handlers=[  # 📤 Specifies where logs are sent
        logging.FileHandler(os.path.join("logs", "logging.log")),  # 📜 Logs to a file named 'logging.log' in the 'logs' directory
        logging.StreamHandler()  # 🖥️ Also logs to the console (standard output)
    ]
)

def configure_llm(MODEL_NAME):  # 🤖 Function to configure the language model (LLM)
    """
    Configure LLM to run on Hugging Face Inference API (Cloud-Based).
    
    Args:
        MODEL_NAME (str): Name of the model to configure (e.g., "qwen-qwq-32b").
    
    Returns:
        llm (LangChain LLM object): Configured model instance, or error message if configuration fails.
    """
    try:
        # logging.info(f"🤖 Querying LLM: {MODEL_NAME}")  # 📝 (Commented) Log the model being queried
        llm = ChatGroq(  # 🌐 Initializes the ChatGroq model for cloud-based inference
            temperature=0,  # 🌡️ Sets temperature to 0 for deterministic responses
            groq_api_key=CONFIG.GROQ_API_KEY,  # 🔑 Uses the Groq API key from config
            model_name=MODEL_NAME  # 📛 Specifies the model name (e.g., "qwen-qwq-32b")
        )
        logging.info(f"✅ {str(MODEL_NAME).capitalize()} Loaded!")  # ✅ Logs success of model loading
        return llm  # 🔄 Returns the configured LLM instance
    except Exception as e:  # ⚠️ Catches any errors during LLM configuration
        logging.error(f"❌ LLM Query Error: {str(e)}")  # ❌ Logs the error details
        return "❌ Error generating LLM response."  # 🚫 Returns an error message if configuration fails