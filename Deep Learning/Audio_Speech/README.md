# Text-to-Speech Streamlit App 🎙️

Welcome to the **Text-to-Speech (TTS) Converter**, a vibrant web application that transforms text into high-quality speech! 🚀 Built with Streamlit and gTTS, this internship project offers a user-friendly interface, customizable options, and robust functionality for learning, presentations, or creative projects. 🌟 Designed for distributed development, it’s modular, well-documented, and ready for team collaboration. 👥

## Features ✨
- **Text-to-Speech Conversion**: Convert text to audio with a single click. 🔊
- **Customizable Options**: Choose from multiple languages (English, French, Spanish, etc.) and toggle slow speech. 🌐🐢
- **In-Browser Playback**: Listen to audio directly in the app, no external players needed. 🎧
- **MP3 Download**: Save audio files for offline use. 💾
- **Conversion History**: View recent conversions with details and playback. 📜
- **Attractive UI**: Dark blue/gray theme, emojis, and smooth styling for a professional look. 🎨
- **Home Page**: Welcoming landing page with an overview and navigation. 🏠
- **Sidebar Guide**: Step-by-step “How to Use” instructions. 📖
- **Robust Backend**: Logging, error handling, and unit tests ensure reliability. 🛠️
- **Distributed Ready**: Modular structure supports team collaboration. 🤝

## Project Structure 📁
```
tts_streamlit_project/
├── src/                    # Core application code
│   ├── tts_engine.py       # TTS conversion logic with gTTS
│   ├── app.py             # Streamlit app with UI
│   └── config.py          # Language and default settings
├── tests/                  # Unit tests
│   └── test_tts_engine.py
├── logs/                   # Log files
│   └── tts_app.log
├── requirements.txt        # Dependencies
├── README.md               # This file
└── .gitignore              # Git ignore
```

## Prerequisites 📋
- **Python 3.8+** 🐍
- **Internet connection** for gTTS 🌐
- **Git** for version control (optional) 📚
- Compatible with Linux, Windows, or macOS 🖥️

## Setup ⚙️
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd tts_streamlit_project
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Requires `streamlit` and `gtts`.*

4. **Ensure Log Directory**:
   ```bash
   mkdir -p logs
   chmod -R u+w logs
   ```

5. **Run the App**:
   ```bash
   streamlit run src/app.py
   ```
   Open `http://localhost:8501` in your browser. 🌍

## Usage 🎮
1. **Home Page 🏠**:
   - View the welcome message and click **Go to Converter 🛠️**.
2. **Converter Page 🔊**:
   - **Enter Text 📝**: Type or paste text in the box.
   - **Select Language 🌐**: Choose from supported languages (e.g., English, French).
   - **Toggle Slow Speech 🐢**: Check for slower audio.
   - **Click Listen 🎧**: Hear the audio in the browser.
   - **Download MP3 💾**: Save the audio file.
   - **View History 📜**: Expand recent conversions for details and playback.
3. **Sidebar 📖**:
   - Read the “How to Use” guide for step-by-step instructions.

## Logging 📝
- Logs are stored in `logs/tts_app.log`. 🗒️
- Check for debugging info (e.g., conversion errors, initialization). 🔍
- Logs rotate to prevent large files. ♻️

## Testing 🧪
- Run unit tests to validate the TTS engine:
  ```bash
  python -m unittest discover tests
  ```
- Tests cover text conversion, invalid inputs, and file handling. ✅

## Deployment 🚀
- **Local**: Run `streamlit run src/app.py` for development. 🖥️
- **Streamlit Cloud**:
  1. Push the repository to GitHub.
  2. Connect to Streamlit Cloud and select the repo.
  3. Set `src/app.py` as the entry point.
  4. Ensure `requirements.txt` is included.
- Audio plays in the browser, and MP3s are downloadable on any platform. 🌐

## Troubleshooting 🛠️
- **No Audio 😔**:
  - Check browser audio permissions (unmute tab). 🔊
  - Ensure internet for gTTS: `ping google.com`. 🌍
  - Verify logs: `cat logs/tts_app.log`. 📜
- **App Not Loading 😞**:
  - Check Streamlit version: `pip install streamlit==1.38.0`. 🐍
  - Clear cache: `rm -rf ~/.streamlit/cache`. 🗑️
- **Errors**:
  - Share `tts_app.log` or terminal output for help. 📧
  - Test manually: `xdg-open output.mp3` (Linux). 🎵

## Contributing 🤝
We welcome contributions! 🎉 Follow these steps:
1. **Fork** the repository. 🍴
2. Create a **feature branch**: `git checkout -b feature/YourFeature`. 🌿
3. **Commit** changes: `git commit -m "Add YourFeature"`. 📝
4. **Push**: `git push origin feature/YourFeature`. 🚀
5. Open a **pull request**. 📬
- Update `README.md` for new features. 📚
- Run tests before submitting. 🧪

## Team Roles 👥
- **TTS Logic**: Enhance `tts_engine.py` (e.g., new engines). 🛠️
- **UI**: Improve `app.py` (e.g., file upload). 🎨
- **Testing**: Add tests in `tests/`. 🧪
- **Docs**: Update `README.md` and guides. 📖

## License 📜
MIT License © 2025


---

Built with ❤️ for internship excellence! 🌟