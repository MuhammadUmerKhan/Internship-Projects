# Real-Time AI Surveillance Application

## Overview
This application provides real-time object detection and tracking of people using a webcam feed. Built with YOLOv8 for detection and DeepSort for tracking, it features a user-friendly Streamlit interface to display the live video feed, detection metrics, and track IDs. The system logs track data to a CSV file and operational logs to a file for debugging and monitoring.

## Features
- **Real-Time Detection**: Identifies people in video frames using YOLOv8.
- **Object Tracking**: Tracks detected individuals across frames with DeepSort, assigning unique IDs.
- **Streamlit UI**: Displays live video with bounding boxes, detection/tracking metrics, and stream controls.
- **Logging**: Saves track IDs with timestamps to `database/entries.csv` and logs operations to `database/app.log`.
- **Camera Support**: Robust camera initialization with fallback indices.

## Folder Structure
- **`run.py`**: Main Streamlit app with a two-tab interface (Overview and Live Stream) for controlling and displaying the video feed.
- **`main.py`**: Standalone script for running the application without Streamlit, using OpenCV for display.
- **`camera.py`**: Handles webcam initialization and frame capture, with fallback for camera indices.
- **`detector.py`**: Performs object detection using YOLOv8, configured for person detection.
- **`tracker.py`**: Manages object tracking with DeepSort, assigning and updating track IDs.
- **`logger.py`**: Logs track IDs and timestamps to a CSV file, with error handling.
- **`utils.py`**: Utility functions for drawing bounding boxes and track IDs on video frames.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd app
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit opencv-python ultralytics deep-sort-realtime
   ```

3. **Download YOLOv8 Model**:
   - Place the `yolov8n.pt` model file in the `weights/` directory. Download from [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics).

4. **Ensure Camera Access**:
   - Verify webcam availability:
     ```bash
     ls /dev/video*
     ```
   - Grant permissions if needed:
     ```bash
     sudo usermod -a -G video $USER
     ```

## Usage
### Streamlit App
1. Run the Streamlit app:
   ```bash
   streamlit run run.py
   ```
2. Open `http://localhost:8501` in a browser.
3. Navigate to the **Live Stream** tab.
4. Click **Start Stream** to view the webcam feed with detection and tracking.
5. Click **Stop Stream** to halt the stream.
6. Check logs in `database/app.log` and track data in `database/entries.csv`.

### Standalone Script
1. Run the standalone script:
   ```bash
   python main.py
   ```
2. View the video feed in a window with bounding boxes and track IDs.
3. Press `q` to exit.
4. Logs are saved to `database/app.log` and `database/entries.csv`.

## Configuration
- **Camera Index**: Default is `1` (`camera.py`). Modify `device_index` in `run.py` or `main.py` if your camera uses a different index (e.g., `/dev/video2`).
- **YOLO Model**: Uses `yolov8n.pt` in `weights/`. Replace with other YOLOv8 models for different performance/accuracy trade-offs.
- **Logging**: Logs are stored in `database/`. Ensure write permissions for the directory.

## Requirements
- **Python**: 3.8+
- **Libraries**: `streamlit`, `opencv-python`, `ultralytics`, `deep-sort-realtime`
- **Hardware**: Webcam, CPU/GPU (GPU recommended for faster YOLOv8 inference)
- **OS**: Linux, macOS, or Windows with webcam drivers

## Troubleshooting
- **Camera Not Found**:
  - Check camera index with `ls /dev/video*` and update `device_index` in `run.py` or `main.py`.
  - Test camera:
    ```bash
    vlc v4l2:///dev/video1
    ```
  - Install drivers:
    ```bash
    sudo apt-get install v4l-utils
    ```
- **Stream Freezes**:
  - Increase `time.sleep(0.03)` in `run.py` to `0.05` for lower CPU usage.
  - Use a lighter YOLO model (e.g., `yolov8n.pt`).
- **Logs**:
  - Check `database/app.log` for errors.
  - Ensure `database/` is writable.