import streamlit as st
import cv2
import numpy as np
from pose_estimator import PoseEstimator
from utils import draw_landmarks
import os
import logging
import time

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

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

# Set page config
st.set_page_config(page_title="Real-Time Pose Estimation", layout="wide", page_icon="🏃‍♂️")

# Inline CSS
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #1e3a8a, #4b5563);
    color: #d1d5db;
    margin: 0;
    padding: 20px;
}
.header {
    background: linear-gradient(90deg, #1e3a8a, #60a5fa);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.header h1 {
    font-size: 2.5em;
    color: #d1d5db;
    margin: 0;
}
.header p {
    font-size: 1.2em;
    color: #d1d5db;
    margin: 10px 0 0;
}
.stButton>button {
    background: linear-gradient(90deg, #60a5fa, #3b82f6);
    color: #d1d5db;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-size: 1em;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
.stButton>button:hover {
    background: linear-gradient(90deg, #3b82f6, #2563eb);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}
.stFileUploader, .stCheckbox {
    background-color: #374151;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}
.stProgress .st-bo {
    background-color: #6b7280;
    border-radius: 5px;
}
.stProgress .st-bo > div {
    background: linear-gradient(90deg, #60a5fa, #3b82f6);
    border-radius: 5px;
}
.sidebar .sidebar-content {
    background-color: #374151;
    border-radius: 10px;
    padding: 15px;
}
.sidebar h2 {
    font-size: 1.8em;
    color: #60a5fa;
    margin-bottom: 15px;
}
.stSidebar .stRadio > div {
    background-color: #4b5563;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #60a5fa;
}
.stMarkdown p {
    color: #d1d5db;
    line-height: 1.6;
}
.footer {
    font-size: 0.9em;
    text-align: center;
    color: #6b7280;
    margin-top: 20px;
}
.container {
    background-color: #374151;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}
.stTabs [data-baseweb="tab-list"] {
    background-color: #4b5563;
    border-radius: 8px;
    padding: 5px;
}
.stTabs [data-baseweb="tab"] {
    color: #d1d5db;
    font-size: 1.1em;
    padding: 10px 20px;
    border-radius: 6px;
    margin: 0 5px;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(90deg, #60a5fa, #3b82f6);
    color: #d1d5db;
}
</style>
""", unsafe_allow_html=True)

# Inline JavaScript
st.markdown("""
<script>
document.querySelectorAll('.stButton>button').forEach(button => {
    button.addEventListener('click', () => {
        button.style.transform = 'scale(0.95)';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
        }, 100);
    });
});
</script>
""", unsafe_allow_html=True)

def home_page():
    """Render the home page with project details."""
    with st.container():
        st.markdown("<div class='header'><h1>Real-Time Pose Estimation 🏃‍♂️</h1><p>Advanced human pose detection for video and webcam input</p></div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("## 📖 Project Overview")
        st.markdown("""
        This professional web application enables real-time human pose estimation using MediaPipe's advanced computer vision technology. 
        Designed for applications in sports analysis, fitness tracking, and human-computer interaction, it supports both video uploads and live webcam feeds.
        The app is optimized for performance across desktop and mobile devices, delivering accurate pose landmarks with a user-friendly interface.
        """)

    with st.container():
        st.markdown("## 🛠️ Tech Stack")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **Python**: Core backend logic")
            st.markdown("- **Streamlit**: Interactive web interface")
            st.markdown("- **MediaPipe**: Pose estimation engine")
        with col2:
            st.markdown("- **OpenCV**: Video and image processing")
            st.markdown("- **NumPy**: Numerical computations")
            st.markdown("- **Logging**: Robust monitoring and debugging")

    with st.container():
        st.markdown("## 🚀 How to Use")
        with st.expander("View Instructions"):
            st.markdown("""
            1. **Navigate**: Use the sidebar to switch between Home and Pose Estimation pages.
            2. **Upload Video** 📹:
               - Select the Pose Estimation page and go to the "Upload Video" tab.
               - Upload a video file (MP4, AVI, MOV).
               - View real-time pose landmarks overlaid on the video.
            3. **Use Webcam** 📷:
               - Select the "Webcam" tab in the Pose Estimation page.
               - Grant browser permissions for camera access.
               - See live pose estimation in your browser.
            4. **Monitor Progress**: A progress bar tracks video processing for uploads.
            """)

    with st.container():
        st.markdown("## ⚙️ Notes")
        st.markdown("""
        - **Webcam Access**: Requires browser permissions and may need HTTPS in production.
        - **Performance**: Ensure sufficient processing power for real-time analysis.
        - **Logs**: Check `logs/app.log` for detailed debugging information.
        """)

def main_page():
    """Render the main pose estimation page with tabs."""
    with st.container():
        st.markdown("<h1>Pose Estimation 🏃‍♂️</h1>", unsafe_allow_html=True)
        st.markdown("<p>Analyze human poses using video uploads or live webcam feed.</p>", unsafe_allow_html=True)

    # Initialize pose estimator
    try:
        pose_estimator = PoseEstimator()
        logger.info("Pose estimator initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize pose estimator: {e}")
        st.error("Failed to initialize pose estimation. Please try again.")
        return

    def process_frame(frame):
        """Process a single frame for pose estimation."""
        try:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose_estimator.process(frame_rgb)
            frame_with_landmarks = draw_landmarks(frame_rgb, results)
            return frame_with_landmarks
        except Exception as e:
            logger.error(f"Error processing frame: {e}")
            return frame

    # Create tabs for video upload and webcam
    tab1, tab2 = st.tabs(["📹 Upload Video", "📷 Webcam"])

    with tab1:
        logger.info("Entered Video Upload tab")
        with st.container():
            st.markdown("### Upload a Video File")
            uploaded_file = st.file_uploader("Select a video (MP4, AVI, MOV)", type=["mp4", "avi", "mov"], key="uploader")
            
            if uploaded_file:
                try:
                    # Save uploaded file temporarily
                    temp_file = "temp_video.mp4"
                    with open(temp_file, "wb") as f:
                        f.write(uploaded_file.read())
                    logger.info(f"Uploaded video saved as {temp_file}")

                    # Process video
                    cap = cv2.VideoCapture(temp_file)
                    if not cap.isOpened():
                        logger.error("Failed to open uploaded video")
                        st.error("Failed to open video file. Please try another file.")
                        return

                    stframe = st.empty()
                    progress = st.progress(0)
                    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    for i in range(frame_count):
                        ret, frame = cap.read()
                        if not ret:
                            break
                        processed_frame = process_frame(frame)
                        if processed_frame is not None:
                            stframe.image(processed_frame, channels="RGB")
                        progress.progress((i + 1) / frame_count)
                        time.sleep(0.03)  # Control frame rate
                    cap.release()
                    os.remove(temp_file)
                    logger.info("Video processing completed and temp file removed")
                except Exception as e:
                    logger.error(f"Error processing video: {e}")
                    st.error("An error occurred while processing the video. Please try again.")
                finally:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                        logger.info("Cleaned up temporary video file")

    with tab2:
        logger.info("Entered Webcam tab")
        with st.container():
            st.markdown("### Live Webcam Feed")
            st.warning("⚠️ Webcam requires browser permissions.")
            if st.button("Start Webcam", key="webcam_button"):
                try:
                    cap = cv2.VideoCapture(0)
                    if not cap.isOpened():
                        logger.error("Failed to access webcam")
                        st.error("Cannot access webcam. Check permissions or device availability.")
                        return
                    stframe = st.empty()
                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            logger.warning("Failed to capture webcam frame")
                            break
                        processed_frame = process_frame(frame)
                        if processed_frame is not None:
                            stframe.image(processed_frame, channels="RGB")
                        time.sleep(0.03)  # Control frame rate
                    cap.release()
                    logger.info("Webcam stream stopped")
                except Exception as e:
                    logger.error(f"Error accessing webcam: {e}")
                    st.error("An error occurred while accessing the webcam. Please check permissions.")
                finally:
                    if 'cap' in locals() and cap.isOpened():
                        cap.release()
                        logger.info("Webcam resources released")

    st.markdown("<p class='footer'>Powered by MediaPipe & Streamlit</p>", unsafe_allow_html=True)

def main():
    """Main function to render the app."""
    # Sidebar navigation
    st.sidebar.markdown("<h2>Navigation 🧭</h2>", unsafe_allow_html=True)
    page = st.sidebar.radio("", ["Home", "Pose Estimation"], label_visibility="collapsed")
    
    if page == "Home":
        home_page()
    else:
        main_page()

if __name__ == "__main__":
    try:
        logger.info("Starting Streamlit app")
        main()
    except Exception as e:
        logger.critical(f"Application crashed: {e}")
        st.error("The application encountered a critical error. Please check logs/app.log.")