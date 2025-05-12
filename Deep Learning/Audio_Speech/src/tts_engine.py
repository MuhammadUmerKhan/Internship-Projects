import logging
import os
import tempfile
from gtts import gTTS

# Configure logging
logging.basic_logger = logging.getLogger(__name__)
if not logging.basic_logger.handlers:
    logging.basic_logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(
        "logs/tts_app.log", maxBytes=1000000, backupCount=5
    )
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logging.basic_logger.addHandler(handler)

class TTSEngine:
    """Handles text-to-speech conversion using gTTS."""
    
    def __init__(self, language="en", slow=False):
        """
        Initialize TTS engine with default settings.
        
        Args:
            language (str): Language code (e.g., 'en').
            slow (bool): Slow speech if True.
        """
        self.language = language
        self.slow = slow
        logging.basic_logger.info(f"TTSEngine initialized with language={language}, slow={slow}")
    
    def convert_to_speech(self, text):
        """
        Convert text to speech and save as MP3.
        
        Args:
            text (str): Text to convert.
        
        Returns:
            str: Path to generated MP3 file, or None if failed.
        """
        if not text or not isinstance(text, str):
            logging.basic_logger.error("Invalid text input provided.")
            return None
        
        try:
            logging.basic_logger.info(f"Converting text: {text[:50]}...")
            
            # Create temporary MP3 file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                filename = tmp_file.name
            
            # Generate MP3
            tts = gTTS(text=text, lang=self.language, slow=self.slow)
            tts.save(filename)
            
            if not os.path.exists(filename):
                logging.basic_logger.error(f"Failed to create MP3 file: {filename}")
                return None
            
            logging.basic_logger.info(f"MP3 generated successfully: {filename}")
            return filename
        
        except Exception as e:
            logging.basic_logger.error(f"Error converting text to speech: {e}")
            return None