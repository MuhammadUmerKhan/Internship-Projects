import os, re, logging, warnings  # 📥 Import os for file operations, re for regex, logging for logs, and warnings for suppression
from langchain.schema import SystemMessage, HumanMessage  # 📥 Import message types for LangChain LLM
from config.config import llm  # 📥 Import config module for LLM configuration
warnings.filterwarnings("ignore")  # ⚠️ Ignore warning messages to keep output clean

# Logging configuration
os.makedirs(os.path.join("logs"), exist_ok=True)  # 📂 Creates a 'logs' directory if it doesn't exist
logging.basicConfig(  # ⚙️ Configures the logging system with specified settings
    level=logging.INFO,  # 📏 Sets logging level to INFO for informational messages and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # 📝 Defines log message format: timestamp, level, and message
    handlers=[  # 📤 Specifies where logs are sent
        logging.FileHandler(os.path.join("logs", "logging.log")),  # 📜 Logs to a file named 'logging.log' in the 'logs' directory
        logging.StreamHandler()  # 🖥️ Also logs to the console (standard output)
    ]
)

def clean_response(response):  # 🧹 Function to clean the LLM response
    return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()  # ✂️ Removes <think> tags and whitespace from the response

def convert_text(roman_text: str) -> str:  # 🔤 Main function to convert Roman Urdu to Urdu script
    message = [  # 📩 Constructs the message list for the LLM
        SystemMessage(content=  # 📜 Defines the system instruction for the LLM
                        """
                You are an expert multilingual Roman script converter with deep knowledge of global linguistics, capable of handling any language spoken in the world. 
                Your task is to:
                1. Detect the language of the input Romanized text (e.g., Romanized Urdu, Romanized Hindi, Romanized Arabic, Romanized Chinese, Romanized Russian, etc.) by analyzing its vocabulary, syntax, and linguistic patterns.
                2. Convert the detected Romanized text into its corresponding clear, grammatically correct, and standardized native script with the following rule:
                   - If the detected language is Romanized Urdu or Romanized Hindi, always convert it to Urdu script (not Devanagari for Hindi).
                   - For all other Romanized languages, convert to their original native scripts (e.g., Arabic script, Chinese characters, Cyrillic script, etc.).
                3. If the input text appears to be incorrectly written or unrecognizable (e.g., random strings like "wrnefihweilfenfwbelfbefbqf"), politely return "Apologies, the text cannot be processed due to unrecognizable input." instead of attempting conversion.
                
                Follow these guidelines:
                - Accurately interpret the intended meaning of the input, correcting any ambiguities, spelling inconsistencies, or errors in phrasing where applicable.
                - Remove unnecessary repetitions, slang, or informal expressions unless they are essential to the meaning.
                - Ensure the output is fluent, natural, and contextually appropriate for formal or semi-formal communication in the detected language.
                - Use proper grammar, punctuation, and vocabulary specific to the language's script to enhance clarity and readability.
                - Output only the converted sentence in the native script without any explanations, translations, or additional text, or the polite message if the input is unrecognizable.
                    """
        ),
        HumanMessage(content=roman_text)  # 💬 Adds the user-provided Romanized text as the human message
    ]
    response = llm(message)  # 🤖 Sends the message to the LLM and gets the response
    logging.info("✅ Translation Done!")  # ✅ Logs success of the translation process
    logging.info("====================================================================================")  # 📏 Adds a separator line to the log
    return clean_response(response.content)  # 🔄 Returns the cleaned Urdu script response

if __name__ == "__main__":  # 🚀 Entry point for running the script directly
    print(convert_text("kasay hain ap?"))  # 🖨️ Tests the function with a sample Roman Urdu input