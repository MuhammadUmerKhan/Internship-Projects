import csv
import os
from datetime import datetime
import logging

# Get logging for this module
logging.basicConfig(filename="camera.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Logger:
    def __init__(self, log_path):
        logging.info(f"Initializing CSV logging with log file: {log_path}")
        self.log_path = log_path
        self.logged_ids = set()
        
        try:
            if not os.path.exists(log_path):
                with open(log_path, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['ID', 'Timestamp'])
                logging.info(f"Created new CSV log file: {log_path}")
            else:
                logging.info(f"Using existing CSV log file: {log_path}")
        except Exception as e:
            logging.error(f"Error initializing CSV log file: {e}")
            raise

    def log(self, track_id):
        if track_id not in self.logged_ids:
            try:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with open(self.log_path, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([track_id, timestamp])
                self.logged_ids.add(track_id)
                logging.info(f"Logged track ID {track_id} at {timestamp}")
            except Exception as e:
                logging.error(f"Error logging track ID {track_id}: {e}")