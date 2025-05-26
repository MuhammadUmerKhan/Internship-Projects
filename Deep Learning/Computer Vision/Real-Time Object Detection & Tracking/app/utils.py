import cv2
import logging

# Get logger for this module
logger = logging.getLogger('utils')

def draw_boxes(frame, tracks, total_count=0):
    logger.debug(f"Drawing {len(tracks)} tracks on frame with total count: {total_count}")
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

    # Draw total count in top right corner
    try:
        text = f'Total Tracked: {total_count}'
        frame_height, frame_width = frame.shape[:2]
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = frame_width - text_size[0] - 10  # 10px padding from right
        text_y = text_size[1] + 10  # 10px padding from top
        cv2.rectangle(frame, (text_x - 5, text_y - text_size[1] - 5), 
                     (text_x + text_size[0] + 5, text_y + 5), (0, 230, 118), -1)  # Green background
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        logger.debug(f"Drew total count: {total_count}")
    except Exception as e:
        logger.error(f"Error drawing total count: {e}")

    return frame