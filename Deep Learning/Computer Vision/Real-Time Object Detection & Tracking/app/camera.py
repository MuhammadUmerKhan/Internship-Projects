import cv2
import logging
import os

# Get logger for this module
logger = logging.getLogger('camera')

class Camera:
    def __init__(self, device_index=1):
        logger.info("Initializing camera")
        self.cap = None

        # Use provided device index or default to 1
        try:
            device_index = int(device_index)
        except ValueError:
            logger.error(f"Invalid device index: {device_index}, defaulting to 1")
            device_index = 1

        # Try camera indices (device_index first, then 0 to 4)
        indices = [device_index] + [i for i in range(5) if i != device_index]
        for index in indices:
            try:
                logger.debug(f"Attempting to open camera at index {index}")
                self.cap = cv2.VideoCapture(index)
                if self.cap.isOpened():
                    logger.info(f"Successfully opened camera at index {index}")
                    return
                else:
                    logger.warning(f"Camera at index {index} could not be opened")
                    self.cap.release()
            except Exception as e:
                logger.error(f"Error trying camera at index {index}: {e}")

        logger.error("No camera could be opened")
        raise RuntimeError("Camera initialization failed: No accessible camera found")

    def get_frame(self):
        try:
            success, frame = self.cap.read()
            if not success:
                logger.warning("Failed to capture frame")
                return None
            logger.debug("Frame captured successfully")
            return frame
        except Exception as e:
            logger.error(f"Error capturing frame: {e}")
            return None

    def release(self):
        try:
            if self.cap is not None:
                self.cap.release()
                logger.info("Camera released")
            else:
                logger.warning("No camera to release")
        except Exception as e:
            logger.error(f"Error releasing camera: {e}")