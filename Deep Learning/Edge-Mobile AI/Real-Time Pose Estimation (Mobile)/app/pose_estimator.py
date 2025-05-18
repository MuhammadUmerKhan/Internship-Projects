import mediapipe as mp
import cv2, os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('logs', 'app.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PoseEstimator:
    def __init__(self):
        try:
            self.mp_pose = mp.solutions.pose
            self.pose = self.mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
            logger.info("PoseEstimator initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PoseEstimator: {e}")
            raise
    
    def process(self, frame):
        """Process a frame and return pose estimation results."""
        try:
            results = self.pose.process(frame)
            logger.debug("Frame processed successfully")
            return results
        except Exception as e:
            logger.error(f"Error processing frame: {e}")
            return None
    
    def close(self):
        """Release resources."""
        try:
            self.pose.close()
            logger.info("PoseEstimator resources released")
        except Exception as e:
            logger.error(f"Error closing PoseEstimator: {e}")