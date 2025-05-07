from flask import Flask, render_template, Response
from app.camera import Camera
from app.detector import Detector
from app.tracker import Tracker
from app.logger import Logger
from app.utils import draw_boxes
import cv2, os

MODEL_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights", "yolov8n.pt"))
CSV_LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "database", "entries.csv"))

app = Flask(__name__)
camera = Camera()
detector = Detector(MODEL_FILE)
tracker = Tracker()
logger = Logger(CSV_LOG_FILE)
# Optional: set these if you want alerts
# alert = Alert(sender_email="you@example.com", password="yourpassword", receiver_email="receiver@example.com")

def generate_frames():
    while True:
        frame = camera.get_frame()
        if frame is None:
            continue

        detections = detector.detect(frame)
        tracks = tracker.update(detections, frame)

        for track in tracks:
            if not track.is_confirmed():
                continue
            logger.log(track.track_id)
            # Uncomment to enable alert
            # alert.send_alert()

        frame = draw_boxes(frame, tracks)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.teardown_appcontext
def shutdown_session(exception=None):
    camera.release()

if __name__ == '__main__':
    app.run(debug=True)
