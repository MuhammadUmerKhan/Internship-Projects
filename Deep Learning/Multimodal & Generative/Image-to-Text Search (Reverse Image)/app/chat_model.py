from app.img_opener import load_image
from app.image_captioning import generate_caption
from utils.utils import configure_llm
from langchain_core.messages import HumanMessage, SystemMessage
import os, logging, re

os.makedirs(os.path.join("logs"), exist_ok=True)  # 📂 Creates a 'logs' directory if it doesn't exist
logging.basicConfig(  # ⚙️ Configures the logging system with specified settings
    level=logging.INFO,  # 📏 Sets logging level to INFO to capture informational messages and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # 📝 Defines log message format: timestamp, level, and message
    handlers=[  # 📤 Specifies where logs are sent
        logging.FileHandler(os.path.join("logs", "logging.log")),  # 📜 Logs to a file named 'logging.log' in the 'logs' directory
        logging.StreamHandler()  # 🖥️ Also logs to the console (standard output)
    ]
)

def generate_scene(caption):
    """
    Refines a raw image caption into a better search query using ChatGroq LLM.
    
    Args:
        caption (str): Raw caption generated from image.
        llm (ChatGroq): Initialized LangChain ChatGroq LLM.
    
    Returns:
        str: Refined, more descriptive query.
    """
    try:
        messages = [
                SystemMessage(content="You are a professional image caption enhancer."),
                HumanMessage(content=f"""
                    The raw image caption is: '{caption}'.

                    Now describe the image in a professional, and well-structured way, always response in english language.
                    - Include background, objects, context, scene type (if possible)
                    - Avoid generic phrases
                    - Keep the tone descriptive and natural
                """)
            ]
        
        llm = configure_llm("qwen-qwq-32b")
        response = llm.invoke(messages)
        cleaned_text = re.sub(r'<think>.*?</think>', '', response.content.strip(), flags=re.DOTALL)        
        logging.info(f"📝 Refined Caption: {cleaned_text}")
        return cleaned_text
    except Exception as e:
        logging.exception(f"❌ Error refining caption: {e}")
        return "❌ Failed to refine caption."

def get_scene_description(image_path):
    image = load_image(image_path)
    caption = generate_caption(image)
    llm_response = generate_scene(caption)
    return llm_response.strip(), caption


if __name__=="__main__":
    print(get_scene_description(os.path.join("..", "assets", "image.jpg")))