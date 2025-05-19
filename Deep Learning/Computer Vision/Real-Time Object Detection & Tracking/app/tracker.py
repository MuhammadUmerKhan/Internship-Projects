from deep_sort_realtime.deepsort_tracker import DeepSort
import logging

# Get logger for this module
logger = logging.getLogger('tracker')

class Tracker:
    def __init__(self):
        logger.info("Initializing DeepSort tracker")
        try:
            self.tracker = DeepSort(max_age=30)
        except Exception as e:
            logger.error(f"Tracker initialization error: {e}")
            raise

    def update(self, detections, frame):
        try:
            logger.debug(f"Updating tracker with {len(detections)} detections")
            tracks = self.tracker.update_tracks(detections, frame=frame)
            logger.debug(f"Tracker returned {len(tracks)} tracks")
            return tracks
        except Exception as e:
            logger.error(f"Tracker update error: {e}")
            return []