# 👁️‍🗨️ Real-Time Person Detection, Tracking, and Logging System with Flask

This project is a **real-time AI surveillance system** that uses computer vision and deep learning to detect and track people via webcam, log their entry times, and display the live feed via a Flask web app. It combines **YOLOv8**, **DeepSORT**, **OpenCV**, and **Flask** into an end-to-end system suitable for security and monitoring use cases.

---

## 📌 Features

| Feature | Description |
|--------|-------------|
| **Real-Time Detection** | Uses YOLOv8 (Ultralytics) to detect people (`class 0`) in the webcam feed. |
| **Multi-Person Tracking** | Assigns persistent IDs to individuals using DeepSORT tracker. |
| **Entry Time Logging** | Each unique person ID is logged once with a timestamp into a CSV file. |
| **Web-Based UI** | Flask web app displays the live video stream on the `/` route. |
| **Modular Codebase** | Clean architecture with separate modules for camera, detection, tracking, logging, alerts, and utilities. |
| **Extensible Alert System** | Includes a ready-to-use `Alert` class to send email notifications during restricted hours (disabled by default). |
| **Logging and Error Handling** | Uses `logging` module to trace camera and system events (`camera.log`). |

---

## 📁 Project Structure

```bash
Real-Time-Person-Tracking/
│
├── app/
│   ├── camera.py       # Webcam capture module (OpenCV)
│   ├── detector.py     # YOLOv8-based person detection
│   ├── tracker.py      # DeepSORT-based multi-object tracking
│   ├── logger.py       # CSV-based entry logging
│   ├── alert.py        # Optional: Email alerts for restricted hours
│   ├── utils.py        # Helper to draw bounding boxes with IDs
│   └── templates/
│       └── index.html  # HTML page for the Flask app
│
├── database/
│   └── entries.csv     # Stores unique person ID + timestamp
│
├── weights/
│   └── yolov8n.pt      # YOLOv8 pre-trained model
│
├── camera.log          # Logs all camera-related events/errors
├── run.py              # Entry-point Flask app
├── requirements.txt    # Dependencies
└── README.md           # Project overview
````

---

## 🚀 How It Works

1. **Webcam Feed** is captured via `cv2.VideoCapture(0)` from `camera.py`.
2. **YOLOv8 Model** detects `person` objects in real time (`detector.py`).
3. **DeepSORT Tracker** assigns IDs and tracks people (`tracker.py`).
4. **Logger** logs each new person only once in `entries.csv` (`logger.py`).
5. **Draw Utility** displays bounding boxes and ID overlays (`utils.py`).
6. **Flask App** serves the live video stream and handles app lifecycle.
7. *(Optional)* `alert.py` can send **email alerts** during restricted hours (before 6 AM or after 10 PM).

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-time-person-tracking.git
cd real-time-person-tracking
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**

* ultralytics
* opencv-python
* flask
* deep\_sort\_realtime
* numpy

> 💡 If not using `requirements.txt`, manually install:

```bash
pip install ultralytics opencv-python flask deep_sort_realtime numpy
```

### 4. Run the Flask App

```bash
python run.py
```

Then open your browser and visit:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🖥️ Sample Output

When the app is running:

* You'll see a **live webcam stream**.
* Each person will be detected and tracked with a green bounding box.
* Their unique ID will appear as `ID: 1`, `ID: 2`, etc.
* Their **entry timestamp** will be saved in `database/entries.csv`.

---

## 📌 Notes

* The webcam index might need to be adjusted:

  * If `cv2.VideoCapture(0)` fails, try `cv2.VideoCapture(1)` in `camera.py`.
* The `yolov8n.pt` file will automatically download from Ultralytics on the first run.
* The `entries.csv` file is created if it doesn't exist.
* `camera.log` logs camera errors and is helpful for debugging.

---

## 📷 Example Screenshot

You can include a screenshot of the web interface with detected bounding boxes here if desired.

---

## 🧠 Tech Stack

| Area              | Tools                                |
| ----------------- | ------------------------------------ |
| **Detection**     | YOLOv8 (Ultralytics)                 |
| **Tracking**      | DeepSORT                             |
| **Webcam Access** | OpenCV                               |
| **Web App**       | Flask                                |
| **Data Logging**  | CSV File                             |
| **Alerts**        | SMTP via Python `smtplib` (Optional) |

---

## 📚 References

* [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com)
* [Deep SORT Tracker](https://github.com/IDOTAI/deep_sort_realtime)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [OpenCV Python Docs](https://docs.opencv.org/)