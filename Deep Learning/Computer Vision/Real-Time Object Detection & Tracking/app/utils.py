import cv2
import logging

# Get logger for this module
logger = logging.getLogger('utils')

def draw_boxes(frame, tracks):
    logger.debug(f"Drawing {len(tracks)} tracks on frame")
    for track in tracks:
        if not track.is_confirmed():
            logger.debug(f"Skipping unconfirmed track ID {track.track_id}")
            continue
        x, y, w, h = track.to_ltrb()
        track_id = track.track_id
        try:
            cv2.rectangle(frame, (int(x), int(y)), (int(w), int(h)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {track_id}', (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            logger.debug(f"Drew box for track ID {track_id}")
        except Exception as e:
            logger.error(f"Error drawing box for track ID {track_id}: {e}")
    return frame