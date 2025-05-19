import logging
import os
import cv2
from camera import Camera
from detector import Detector
from tracker import Tracker
from logger import Logger
from utils import draw_boxes

# Configure logging
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database"))
LOG_FILE = os.path.join(LOG_DIR, "app.log")
MODEL_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "weights", "yolov8n.pt"))
CSV_LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database", "entries.csv"))

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('main')

logger.info("Starting real-time tracking application")

try:
    camera = Camera()
    detector = Detector(MODEL_FILE)
    tracker = Tracker()
    logger_csv = Logger(CSV_LOG_FILE)
except Exception as e:
    logger.error(f"Initialization failed: {e}")
    exit(1)

try:
    while True:
        frame = camera.get_frame()
        if frame is None:
            logger.warning("Skipping frame due to capture failure")
            continue
            
        detections = detector.detect(frame=frame)
        tracks = tracker.update(detections=detections, frame=frame)
        frame = draw_boxes(frame=frame, tracks=tracks)
        
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            logger_csv.log(track_id=track_id)
        
        cv2.imshow("Real-Time Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("User requested exit")
            break
except KeyboardInterrupt:
    logger.info("Application interrupted by user")
except Exception as e:
    logger.error(f"Runtime error: {e}")
finally:
    camera.release()
    cv2.destroyAllWindows()
    logger.info("Application shutdown complete")