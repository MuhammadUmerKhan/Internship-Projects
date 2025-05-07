import cv2
import logging

# Get logging for this module
logging.basicConfig(filename="camera.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Camera:
    def __init__(self):
        logging.info("Initializing camera")
        try:
            self.cap = cv2.VideoCapture(1)
            if not self.cap.isOpened():
                logging.error("Failed to open camera")
                raise RuntimeError("Camera initialization failed")
        except Exception as e:
            logging.error(f"Camera initialization error: {e}")
            raise

    def get_frame(self):
        try:
            success, frame = self.cap.read()
            if not success:
                logging.warning("Failed to capture frame")
                return None
            logging.debug("Frame captured successfully")
            return frame
        except Exception as e:
            logging.error(f"Error capturing frame: {e}")
            return None

    def release(self):
        try:
            self.cap.release()
            logging.info("Camera released")
        except Exception as e:
            logging.error(f"Error releasing camera: {e}")