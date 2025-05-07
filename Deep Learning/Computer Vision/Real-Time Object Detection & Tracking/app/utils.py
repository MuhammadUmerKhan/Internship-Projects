import cv2
import logging

# Get logger for this module
logging.basicConfig(filename="camera.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def draw_boxes(frame, tracks):
    logging.debug(f"Drawing {len(tracks)} tracks on frame")
    for track in tracks:
        if not track.is_confirmed():
            logging.debug(f"Skipping unconfirmed track ID {track.track_id}")
            continue
        x, y, w, h = track.to_ltrb()
        track_id = track.track_id
        try:
            cv2.rectangle(frame, (int(x), int(y)), (int(w), int(h)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {track_id}', (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            logging.debug(f"Drew box for track ID {track_id}")
        except Exception as e:
            logging.error(f"Error drawing box for track ID {track_id}: {e}")
    return frame