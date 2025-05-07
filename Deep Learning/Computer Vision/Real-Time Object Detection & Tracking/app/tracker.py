from deep_sort_realtime.deepsort_tracker import DeepSort
import logging

# Get logger for this module
logging.basicConfig(filename="camera.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Tracker:
    def __init__(self):
        logging.info("Initializing DeepSort tracker")
        try:
            self.tracker = DeepSort(max_age=30)
        except Exception as e:
            logging.error(f"Tracker initialization error: {e}")
            raise

    def update(self, detections, frame):
        try:
            logging.debug(f"Updating tracker with {len(detections)} detections")
            tracks = self.tracker.update_tracks(detections, frame=frame)
            logging.debug(f"Tracker returned {len(tracks)} tracks")
            return tracks
        except Exception as e:
            logging.error(f"Tracker update error: {e}")
            return []