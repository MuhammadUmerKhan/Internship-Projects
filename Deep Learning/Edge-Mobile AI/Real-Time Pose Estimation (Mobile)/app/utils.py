import cv2, os
import mediapipe as mp
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

def draw_landmarks(frame, results):
    """Draw pose landmarks on the frame."""
    try:
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
        if results and results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )
            logger.debug("Landmarks drawn on frame")
        else:
            logger.warning("No landmarks detected in frame")
        return frame
    except Exception as e:
        logger.error(f"Error drawing landmarks: {e}")
        return frame