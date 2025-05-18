# App Folder: Real-Time Pose Estimation (Mobile) 🏃‍♂️

The `app` folder contains the core Python scripts for the Real-Time Pose Estimation (Mobile) project, a Streamlit-based web application for real-time human pose detection using MediaPipe and OpenCV. This folder encapsulates the application's frontend, pose estimation logic, and utility functions, serving as the backbone of the project.

## 📂 Purpose

The `app` folder houses all Python scripts responsible for:
- Rendering the Streamlit web interface with a modern, tab-based UI.
- Processing video uploads and live webcam feeds for pose estimation.
- Handling pose detection and visualization of landmarks.
- Implementing robust logging and error handling for debugging and reliability.

## 📋 Files Overview

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `__init__.py`       | Marks the `app` directory as a Python package, enabling module imports.     |
| `main.py`           | Entry point for the Streamlit app, defining the UI, tabs (📹 Upload Video, 📷 Webcam), and navigation logic. |
| `pose_estimator.py` | Implements the `PoseEstimator` class for MediaPipe-based pose detection.    |
| `utils.py`          | Contains utility functions, such as `draw_landmarks`, for visualizing poses. |

### Detailed File Descriptions

1. **`__init__.py`**:
   - An empty file that designates the `app` folder as a Python package.
   - Enables importing modules (e.g., `from app.pose_estimator import PoseEstimator`).

2. **`main.py`**:
   - **Purpose**: Serves as the Streamlit application entry point.
   - **Key Features**:
     - Defines the app layout with a sidebar for navigation (Home, Pose Estimation).
     - Implements two tabs in the Pose Estimation page: 📹 Upload Video and 📷 Webcam.
     - Handles video file uploads (MP4, AVI, MOV) with progress tracking.
     - Manages live webcam feeds with a "Start Webcam" button.
     - Uses inline CSS for a dark-themed, responsive UI and inline JavaScript for button animations.
     - Integrates logging and try-except blocks for robust error handling.
   - **Dependencies**: Imports `PoseEstimator` from `pose_estimator.py` and `draw_landmarks` from `utils.py`.

3. **`pose_estimator.py`**:
   - **Purpose**: Encapsulates pose estimation logic using MediaPipe.
   - **Key Features**:
     - Defines the `PoseEstimator` class with methods for initialization, frame processing, and resource cleanup.
     - Configures MediaPipe's pose model with detection and tracking confidence thresholds.
     - Includes logging for initialization and errors, with try-except blocks for reliability.
   - **Dependencies**: Requires `mediapipe` and `cv2` (OpenCV).

4. **`utils.py`**:
   - **Purpose**: Provides utility functions for pose visualization.
   - **Key Features**:
     - Implements `draw_landmarks` to overlay pose landmarks on video frames.
     - Uses MediaPipe's drawing utilities for consistent visualization.
     - Includes logging and error handling to manage missing landmarks or processing errors.
   - **Dependencies**: Requires `mediapipe` and `cv2` (OpenCV).

## 🛠️ Key Implementation Details

- **Logging**: All scripts use Python's `logging` module to log events (e.g., initialization, tab navigation, errors) to `logs/app.log` and the console. The log format includes timestamps, module names, and levels (INFO, ERROR, etc.).
- **Error Handling**: Try-except blocks ensure robust handling of errors (e.g., file I/O, webcam access, frame processing), with user-friendly messages displayed via Streamlit.
- **Modularity**: The scripts are modular, with `main.py` orchestrating the UI and logic, `pose_estimator.py` handling core pose detection, and `utils.py` managing visualization.
- **UI Design**: Inline CSS in `main.py` creates a dark-themed, responsive interface (no white colors), with gradients, shadows, and tab styling. Inline JavaScript adds button click animations.
- **Performance**: Optimized for mobile and desktop using lightweight MediaPipe models and efficient OpenCV processing.

## 🚀 Usage within the Project

To run the application, execute:
```bash
streamlit run app/main.py
```

This launches the Streamlit app, which relies on the scripts in the `app` folder to:
1. Render the Home page with project details and instructions.
2. Provide the Pose Estimation page with tabs for video uploads and webcam feeds.
3. Process video or webcam input to detect and visualize human poses in real-time.

## 📝 Notes for Developers

- **Extending the App**:
  - Add new tabs in `main.py` by modifying the `st.tabs` call in `main_page`.
  - Enhance `pose_estimator.py` with custom MediaPipe configurations (e.g., adjust confidence thresholds).
  - Add utility functions to `utils.py` for advanced visualizations or analytics.
- **Debugging**:
  - Check `logs/app.log` for detailed logs, including script-specific events (e.g., "Entered Video Upload tab").
  - Use error messages in the UI to identify issues like webcam permission errors.
- **Dependencies**:
  - Ensure all dependencies (`streamlit`, `opencv-python`, `mediapipe`, `numpy`) are installed via `requirements.txt`.
  - See the project-level `README.md` for installation instructions.
- **Webcam Support**:
  - Webcam functionality may require HTTPS in production due to browser security restrictions.
  - Test webcam access locally to ensure permissions are granted.

## 🔗 Related Resources

- **Project-Level README**: See `../README.md` for installation, usage, and project-wide details.
- **Logs**: Review `../logs/app.log` for runtime logs generated by these scripts.
- **Requirements**: Check `../requirements.txt` for dependency versions.