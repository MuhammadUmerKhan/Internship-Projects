from ultralytics import YOLO
import numpy as np
import logging

# Get logger for this module
logger = logging.getLogger('detector')

class Detector:
    def __init__(self, model_path):
        logger.info(f"Initializing YOLO detector with model: {model_path}")
        try:
            self.model = YOLO(model_path)
        except Exception as e:
            logger.error(f"Detector initialization error: {e}")
            raise

    def detect(self, frame):
        try:
            logger.debug("Running YOLO detection")
            results = self.model.predict(source=frame, conf=0.4, classes=[0], stream=False)
            detections = []
            for result in results:
                boxes = result.boxes.cpu().numpy()
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    conf = float(box.conf[0])
                    detections.append([[float(x1), float(y1), float(x2), float(y2)], conf, 0])
            logger.debug(f"Detected {len(detections)} objects")
            return detections
        except Exception as e:
            logger.error(f"Detection error: {e}")
            return []