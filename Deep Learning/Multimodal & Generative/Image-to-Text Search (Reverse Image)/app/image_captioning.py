from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch, os, logging
from app.img_opener import load_image

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
    # Load once
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    logging.info("✅ Model Found!")
except Exception as e:
    print(f"❌ {e}")
    logging.error(f"❌ {e}")

def generate_caption(image: Image.Image) -> str:
    input = processor(image, return_tensors='pt')
    with torch.no_grad():
        out = model.generate(**input)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

if __name__=="__main__":
    image = load_image(os.path.join("..", "assets", "image.jpg"))
    print(generate_caption(image))