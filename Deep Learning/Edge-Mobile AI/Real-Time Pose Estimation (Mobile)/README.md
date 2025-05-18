# Real-Time Pose Estimation (Mobile) 🏃‍♂️

A professional, Streamlit-based web application for real-time human pose estimation using MediaPipe and OpenCV. This app supports video uploads and live webcam feeds, optimized for both desktop and mobile devices, making it ideal for applications in sports analysis, fitness tracking, and human-computer interaction.

## 🎯 Key Features

- **Real-Time Pose Detection**: Accurately detects and visualizes human body landmarks using MediaPipe's pose estimation model.
- **Video Upload Support**: Upload MP4, AVI, or MOV files to analyze pre-recorded videos with a progress bar for processing.
- **Live Webcam Feed**: Stream live pose estimation from your webcam with browser permission support.
- **Modern UI**: Sleek, dark-themed interface with tabs for video upload (📹) and webcam (📷), built with inline CSS and JavaScript.
- **Responsive Design**: Optimized for mobile and desktop, ensuring cross-device compatibility.
- **Robust Logging**: Logs all key events and errors to `logs/app.log` for debugging and monitoring.
- **Error Handling**: Comprehensive try-except blocks provide user-friendly error messages and resource cleanup.

## 🛠️ Tech Stack

- **Python 3.8+**: Core programming language for backend logic.
- **Streamlit 1.39.0**: Framework for building the interactive web interface.
- **MediaPipe 0.10.14**: Google's open-source library for pose estimation.
- **OpenCV 4.10.0.84**: Handles video processing and frame manipulation.
- **NumPy 2.1.1**: Supports efficient numerical computations.
- **Logging**: Python's standard library for robust monitoring and debugging.

## 📋 Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system.
- **Virtual Environment**: Recommended for dependency isolation.
- **Webcam** (optional): Required for live feed functionality.
- **Browser**: Modern browser (e.g., Chrome, Firefox) for accessing the app.

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd real-time-pose-estimation
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app/main.py
   ```

5. **Access the App**: Open `http://localhost:8501` in your browser.

## 🖥️ Usage

1. **Navigate the App**:
   - Use the sidebar (🧭 Navigation) to switch between **Home** and **Pose Estimation** pages.
   - The **Home** page provides an overview, tech stack, usage instructions, and notes.
   - The **Pose Estimation** page contains two tabs: 📹 Upload Video and 📷 Webcam.

2. **Upload Video (📹)**:
   - In the Pose Estimation page, select the "Upload Video" tab.
   - Upload a video file (MP4, AVI, MOV).
   - Watch real-time pose landmarks overlaid on the video, with a progress bar tracking processing.

3. **Use Webcam (📷)**:
   - In the Pose Estimation page, select the "Webcam" tab.
   - Click the "Start Webcam" button and grant browser permissions.
   - View live pose estimation in your browser.

4. **Monitor Logs**:
   - Check `logs/app.log` for detailed debugging information, including initialization, processing, and error logs.

## 📂 Folder Structure

```
real-time-pose-estimation/
├── app/
│   ├── __init__.py          # Marks directory as Python package
│   ├── main.py              # Streamlit app entry point with UI and tabs
│   ├── pose_estimator.py    # Pose estimation logic using MediaPipe
│   └── utils.py             # Utility functions for drawing landmarks
├── logs/
│   └── app.log              # Log file for debugging and monitoring
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignores unnecessary files
```

## 📝 Notes

- **Webcam Support**: Requires browser permissions and may need HTTPS for production deployment (e.g., via Heroku or AWS with SSL).
- **Performance**: Ensure your device has sufficient processing power for real-time video analysis, especially on mobile.
- **Mobile Optimization**: MediaPipe is lightweight, but test on mobile devices to confirm performance.
- **Logging**: The `logs/app.log` file is created automatically and logs key events (e.g., app start, tab navigation, errors).
- **Extensibility**: The app can be extended with additional features (e.g., pose analytics, settings tab) by modifying `main.py`.

## 🐛 Debugging

- **Check Logs**: Review `logs/app.log` for detailed error messages and event logs.
- **Common Issues**:
  - **Webcam Errors**: Ensure browser permissions are granted and no other app is using the camera.
  - **Video Errors**: Verify the video format (MP4, AVI, MOV) and file integrity.
  - **Performance Lag**: Reduce video resolution or frame rate in `main.py` (adjust `time.sleep`).
- **Contact**: For support, raise an issue on the repository or contact the maintainer.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- **MediaPipe**: For providing a robust pose estimation framework.
- **Streamlit**: For enabling rapid development of interactive web apps.
- **OpenCV**: For powerful video processing capabilities.