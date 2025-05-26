# Real-Time AI Surveillance Project 🚀🔍

## 📖 Overview
The **Real-Time AI Surveillance** project is a powerful application designed to detect and track people in real-time using a webcam feed. Leveraging **YOLOv8** for object detection and **DeepSort** for tracking, it provides a robust solution for security and monitoring tasks. The project includes a **Streamlit-based web interface** for live video display and control, alongside a standalone script for terminal-based execution. All activities are logged to a CSV file and a detailed log file for auditing and debugging. 🕵️‍♂️📹

### 🎯 Key Features
- **Real-Time Detection** 🕒: Identifies people in video frames with YOLOv8’s high-accuracy model.
- **Persistent Tracking** 🏷️: Tracks individuals across frames using DeepSort, assigning unique IDs.
- **Interactive UI** 🌐: Streamlit app with tabs for project overview and live streaming, featuring start/stop controls and metrics.
- **Comprehensive Logging** 📝: Saves track IDs with timestamps to `database/entries.csv` and operational logs to `database/app.log`.
- **Flexible Camera Support** 📷: Robust camera initialization with fallback indices for reliable webcam access.
- **Customizable** ⚙️: Easily adjust camera indices, YOLO models, or logging levels.

## 📂 Project Structure
The project is organized into two main directories: `app` (core application files) and `database` (logging outputs). Below is the structure with file descriptions:

- **📁 app/**: Contains the application’s source code.
  - `run.py` 🌐: Main Streamlit app with a two-tab interface (Overview, Live Stream) for controlling and displaying the video feed with bounding boxes and metrics.
  - `main.py` 🖥️: Standalone script for running the application without Streamlit, using OpenCV for video display.
  - `camera.py` 📷: Manages webcam initialization and frame capture, with fallback logic for camera indices.
  - `detector.py` 🔎: Performs object detection using YOLOv8, configured for person detection (`class=0`).
  - `tracker.py` 🏃: Handles object tracking with DeepSort, updating track IDs across frames.
  - `logger.py` 📋: Logs unique track IDs and timestamps to `database/entries.csv`.
  - `utils.py` 🎨: Utility functions for drawing bounding boxes and track IDs on video frames.

- **📁 database/**: Stores logging outputs.
  - `entries.csv` 📊: CSV file logging unique track IDs and timestamps (e.g., `ID,Timestamp`).
  - `app.log` 🖹: Text file with detailed operational logs (e.g., initialization, errors, frame processing).

- **📁 weights/** (not included, required): Stores the YOLOv8 model file (`yolov8n.pt`).

## 🛠️ Setup
Follow these steps to get the project up and running:

1. **Clone the Repository** 📥:
   ```bash
   git clone <repository-url>
   cd surveillance-project
   ```

2. **Create Required Directories** 🗂️:
   ```bash
   mkdir -p app database weights
   ```

3. **Install Dependencies** 📦:
   ```bash
   pip install streamlit opencv-python ultralytics deep-sort-realtime
   ```

4. **Download YOLOv8 Model** 🧠:
   - Download `yolov8n.pt` from [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics).
   - Place it in the `weights/` directory:
     ```bash
     mv yolov8n.pt weights/
     ```

5. **Verify Camera Access** 📷:
   - Check available cameras:
     ```bash
     ls /dev/video*
     ```
   - Grant permissions if needed:
     ```bash
     sudo usermod -a -G video $USER
     ```
     Log out and back in.
   - Test camera:
     ```bash
     vlc v4l2:///dev/video1
     ```

6. **Ensure Folder Permissions** 🔒:
   ```bash
   chmod -R u+w database/
   ```

## 🚀 Usage
The project offers two ways to run the application: via the **Streamlit web interface** or as a **standalone script**.

### Option 1: Streamlit Web Interface 🌐
1. Run the Streamlit app:
   ```bash
   streamlit run run.py
   ```
2. Open `http://localhost:8501` in a browser.
3. Navigate to the **Overview** tab to learn about the project. 📘
4. Go to the **Live Stream** tab:
   - Click **Start Stream** to begin the webcam feed with real-time detection and tracking. ▶️
   - View bounding boxes, track IDs, and metrics (detections, tracks).
   - Click **Stop Stream** to halt the stream. ⏹️
5. Monitor logs:
   - Track data: `database/entries.csv`
   - Operational logs: `database/app.log`

### Option 2: Standalone Script 🖥️
1. Run the standalone script:
   ```bash
   python app/main.py
   ```
2. A window opens displaying the video feed with bounding boxes and track IDs.
3. Press `q` to exit. 🚪
4. Logs are saved to `database/entries.csv` and `database/app.log`.

## ⚙️ Configuration
Customize the application by modifying the following:

- **Camera Index** 📷:
  - Default: `device_index=1` in `app/camera.py`.
  - If your camera is at a different index (e.g., `/dev/video2`), update `run.py` or `main.py`:
    ```python
    st.session_state.camera = Camera(device_index=2)  # in run.py
    camera = Camera(device_index=2)  # in main.py
    ```

- **YOLO Model** 🧠:
  - Default: `yolov8n.pt` in `weights/`.
  - Replace with other YOLOv8 models (e.g., `yolov8s.pt` for better accuracy, `yolov8n.pt` for speed) in `run.py` and `main.py`:
    ```python
    MODEL_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "weights", "yolov8s.pt"))
    ```

- **Logging Level** 📝:
  - Default: `INFO` in `run.py`, `DEBUG` in `main.py`.
  - Change in `run.py` or `main.py` for more/less detail:
    ```python
    logging.basicConfig(level=logging.DEBUG)  # More verbose
    ```

- **Detection Confidence** 🔎:
  - Default: `conf=0.4` in `detector.py`.
  - Adjust for sensitivity:
    ```python
    results = self.model.predict(source=frame, conf=0.3, classes=[0], stream=False)
    ```

## 📋 Logging
The application generates two types of logs:

- **`database/entries.csv`** 📊:
  - Stores unique track IDs and timestamps.
  - Format: `ID,Timestamp` (e.g., `1,2025-05-19 10:52:00`).
  - Use for tracking activity analysis.

- **`database/app.log`** 🖹:
  - Logs operational details (e.g., initialization, errors, frame processing).
  - Format: `YYYY-MM-DD HH:MM:SS [LEVEL] MODULE: MESSAGE`.
  - Example:
    ```
    2025-05-19 10:52:00,000 [INFO] streamlit: Stream initialized.
    2025-05-19 10:52:00,100 [INFO] camera: Successfully opened camera at index 1
    ```
  - Use for debugging and monitoring.

## 🧰 Requirements
- **Python**: 3.8+ 🐍
- **Libraries**:
  - `streamlit` 🌐
  - `opencv-python` 📷
  - `ultralytics` 🔎
  - `deep-sort-realtime` 🏃
- **Hardware**: Webcam, CPU/GPU (GPU recommended for YOLOv8) 💻
- **OS**: Linux, macOS, or Windows with webcam drivers 🖥️
- **Model File**: `yolov8n.pt` in `weights/` 🧠

## 🛡️ Troubleshooting
- **Camera Not Found** 🚨:
  - Check camera index:
    ```bash
    ls /dev/video*
    ```
    Update `device_index` in `run.py` or `main.py`.
  - Test camera:
    ```bash
    vlc v4l2:///dev/video1
    ```
  - Install drivers:
    ```bash
    sudo apt-get install v4l-utils
    ```
  - Check `database/app.log` for errors like:
    ```
    [ERROR] camera: No camera could be opened
    ```

- **Video Not Displaying in Streamlit** 😕:
  - Ensure `run.py` uses `st.rerun` (already implemented in provided code).
  - Clear Streamlit cache:
    ```bash
    rm -rf ~/.streamlit/cache
    ```
  - Update Streamlit:
    ```bash
    pip install --upgrade streamlit
    ```

- **Stream Lags** 🐢:
  - Increase `time.sleep(0.03)` to `0.05` in `run.py`:
    ```python
    time.sleep(0.05)  # 20 FPS
    ```
  - Use a lighter YOLO model (e.g., `yolov8n.pt`).
  - Check CPU/GPU usage.

- **Log Files Missing or Empty** 📭:
  - Ensure `database/` exists and is writable:
    ```bash
    mkdir -p database
    chmod -R u+w database/
    ```
  - Check `app.log` for initialization errors.

- **Large Log Files** 📈:
  - Rotate or clear `app.log`:
    ```bash
    > database/app.log
    ```
  - Use a log rotation tool for production.

## 📜 License
This project is licensed under the **MIT License**. 📄

## 🙌 Contributing
Contributions are welcome! Please:
1. Fork the repository. 🍴
2. Create a feature branch (`git checkout -b feature/AmazingFeature`). 🌿
3. Commit changes (`git commit -m 'Add AmazingFeature'`). 💾
4. Push to the branch (`git push origin feature/AmazingFeature`). 🚀
5. Open a Pull Request. 📬

## 📬 Contact
For questions or feedback, open an issue or contact the maintainers. 📧