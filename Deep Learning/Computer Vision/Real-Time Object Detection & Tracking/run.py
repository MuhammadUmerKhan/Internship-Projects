import streamlit as st
import cv2
import logging
import os
from app.camera import Camera
from app.detector import Detector
from app.tracker import Tracker
from app.logger import Logger
from app.utils import draw_boxes

# Configure paths
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "database"))
LOG_FILE = os.path.join(LOG_DIR, "app.log")
MODEL_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights", "yolov8n.pt"))
CSV_LOG_FILE = os.path.join(LOG_DIR, "entries.csv")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('streamlit')

# Streamlit page config
st.set_page_config(page_title="AI Surveillance", layout="wide", page_icon="🎥")

# CSS Styling
st.markdown("""
<style>
body {
    background-color: #121212;
    color: #ffffff;
}
.main {
    background-color: #121212;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
    padding: 20px;
}
.header {
    text-align: center;
    font-size: 2.5rem;
    color: #00e676;
    margin-bottom: 1rem;
}
.video-frame {
    border: 2px solid #00e676;
    border-radius: 8px;
    margin-bottom: 20px;
}
.metrics {
    display: flex;
    justify-content: center;
    gap: 40px;
    font-size: 1.1rem;
    margin-top: 1rem;
}
.metric-label {
    color: #00e676;
    font-weight: bold;
}
.status {
    text-align: center;
    font-size: 1rem;
    color: #00e676;
    margin-top: 10px;
}
.stButton>button {
    background-color: #00e676;
    color: #121212;
    border: none;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    font-size: 16px;
    width: 100%;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #00c853;
    color: #ffffff;
}
.intro-section {
    max-width: 850px;
    margin: auto;
    font-size: 1.05rem;
    line-height: 1.75;
}
.intro-section h2 {
    color: #00e676;
    font-size: 1.5rem;
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# Session state
for key in ["streaming", "camera", "detector", "tracker", "logger_csv"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "streaming" else False

# Tabs
intro_tab, stream_tab = st.tabs(["📘 Overview", "🎥 Live Stream"])

# Overview Tab
with intro_tab:
    st.markdown('<div class="intro-section">', unsafe_allow_html=True)
    st.markdown("""
    ## 🎯 Welcome to AI Surveillance System
    
    🔍 **Track. Detect. Monitor.** This app transforms your webcam into an intelligent surveillance tool powered by cutting-edge AI.

    Using **YOLOv8** and **DeepSort**, it detects and tracks multiple people in real time, while logging the activity for further insights. It's fast, lightweight, and customizable!

    ### 🧠 How It Works:
    - 👁️ Live feed from your webcam is captured.
    - 🧠 YOLOv8 detects people and their locations.
    - 📌 DeepSort assigns consistent IDs and tracks movement.
    - 🗂️ Each detection is logged in real-time to a CSV file.

    ### 🔧 Tech Stack:
    - 🐍 **Python 3.8+**
    - 🧠 **YOLOv8** (Object Detection)
    - 🔄 **DeepSort** (Object Tracking)
    - 🧰 **OpenCV** (Video handling)
    - 🎈 **Streamlit** (Web app UI)
    - 📋 **CSV Logging** (For record keeping)

    ### 🚀 How To Use:
    1. Go to the **🎥 Live Stream** tab
    2. Click **▶️ Start Stream** to begin surveillance
    3. Watch real-time detections & tracking IDs appear on screen
    4. Click **⏹️ Stop Stream** to end the session and finalize logs

    ### 📦 Prerequisites:
    - ✅ Python installed with required libraries
    - 🎥 Functional webcam
    - 📁 Access to `weights/yolov8n.pt` model file

    ---  
    This system is ideal for **smart monitoring**, **entry logging**, or building intelligent CCTV systems at low cost.  
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Stream Tab
with stream_tab:
    st.markdown('<div class="header">🔴 AI-Powered Surveillance Stream</div>', unsafe_allow_html=True)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        start_button = st.button("▶️ Start Stream")
    with col2:
        stop_button = st.button("⏹️ Stop Stream")
    st.markdown("</div>", unsafe_allow_html=True)

    if start_button and not st.session_state.streaming:
        try:
            st.session_state.camera = Camera(device_index=1)
            st.session_state.detector = Detector(MODEL_FILE)
            st.session_state.tracker = Tracker()
            st.session_state.logger_csv = Logger(CSV_LOG_FILE)
            st.session_state.streaming = True
            logger.info("Stream initialized.")
        except Exception as e:
            logger.error(f"Init failed: {e}")
            st.error(f"Initialization failed: {e}")

    if stop_button and st.session_state.streaming:
        if st.session_state.camera:
            st.session_state.camera.release()
        for key in ["streaming", "camera", "detector", "tracker", "logger_csv"]:
            st.session_state[key] = None if key != "streaming" else False
        logger.info("Stream stopped.")

    video_placeholder = st.empty()
    metrics_placeholder = st.empty()
    status_placeholder = st.empty()

    if st.session_state.streaming and st.session_state.camera:
        status_placeholder.markdown('<div class="status">✅ Stream Active — Detecting and Logging</div>', unsafe_allow_html=True)
        while st.session_state.streaming:
            try:
                frame = st.session_state.camera.get_frame()
                if frame is None:
                    continue
                detections = st.session_state.detector.detect(frame)
                tracks = st.session_state.tracker.update(detections, frame)
                confirmed_tracks = [track for track in tracks if track.is_confirmed()]

                for track in confirmed_tracks:
                    st.session_state.logger_csv.log(track.track_id)

                frame = draw_boxes(frame, tracks)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                video_placeholder.image(rgb_frame, channels="RGB", use_column_width=True, caption="📹 Real-Time Video Feed")

                metrics_placeholder.markdown(f"""
                <div class='metrics'>
                    <div><span class='metric-label'>🧍‍♂️ Detections:</span> {len(detections)}</div>
                    <div><span class='metric-label'>🆔 Active Tracks:</span> {len(confirmed_tracks)}</div>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                logger.error(f"Streaming error: {e}")
                status_placeholder.markdown(f'<div class="status">❌ Error: {e}</div>', unsafe_allow_html=True)
                break
    else:
        status_placeholder.markdown('<div class="status">⛔ Stream Stopped</div>', unsafe_allow_html=True)

# Cleanup
@st.cache_resource
def cleanup():
    if st.session_state.camera:
        st.session_state.camera.release()
    logger.info("Cleaned up resources.")
