# 🖼️🔍 Image-to-Text Search Project

## 📖 Introduction
Welcome to the **Image-to-Text Search** project! 🎉 This application transforms images into detailed textual descriptions using advanced AI models. It’s perfect for reverse image search, storytelling, and content understanding. Built with a sleek Streamlit interface, this project leverages BLIP-2 for image captioning and Qwen (via Groq API) for refining captions into professional scene descriptions.

## 🌟 Features
- 📷 **Image Upload & Processing**: Upload any image (JPG, JPEG, PNG) and get a detailed description.
- 🧠 **AI-Powered Captioning**: Uses BLIP-2 to generate raw captions and Qwen (via Groq API) to refine them.
- 🎨 **Modern UI**: Streamlit-based interface with gradient backgrounds, animations, and responsive design.
- 📜 **Logging**: Comprehensive logging to `logs/logging.log` and console for debugging.
- 🌐 **Modular Code**: Clean, organized code structure with separate modules for app logic, configuration, and utilities.

## 📂 Folder Structure
- **app/**: Core application logic.
  - `main.py`: Streamlit app with UI and image processing.
  - `img_opener.py`: Loads images using PIL.
  - `image_captioning.py`: Generates captions using BLIP-2.
  - `chat_model.py`: Refines captions into scene descriptions using Qwen.
- **config/**: Configuration settings.
  - `config.py`: Loads environment variables (e.g., API keys) and configures the LLM.
- **utils/**: Utility functions.
  - `utils.py`: Configures the ChatGroq LLM for inference.
- **assets/**: Stores sample images (e.g., `image.jpg`) for testing.
- **logs/**: Stores log files (e.g., `logging.log`).
- **requirements.txt**: Lists all Python dependencies.
- **.env**: Stores environment variables like `GROQ_API_KEY` (not tracked in version control).

## 🛠️ Tech Stack
- **Frontend**: Streamlit + Custom CSS 🎨
- **Image Processing**: BLIP-2 (Salesforce) via `transformers` 🖼️
- **Language Model**: Qwen (via Groq API) using `langchain_groq` 🤖
- **Dependencies**: Python, PIL, PyTorch, `python-dotenv`, and more (see `requirements.txt`).
- **Logging**: Python `logging` module 📜

## ⚙️ Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```
4. **Ensure Assets**:
   - Place a sample image (e.g., `image.jpg`) in the `assets` folder for testing.

## 🚀 Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```
2. Open your browser (usually at `http://localhost:8501`).
3. Navigate to the "Upload Image" tab, upload an image, and view the generated scene description.

## 📈 Outcome
The project successfully transforms images into detailed, professional scene descriptions. For example:
- **Input**: An image of a sunset over a beach.
- **Output**: "A serene beach scene at sunset, with the sky painted in hues of orange and pink. Gentle waves lap against the sandy shore, while seagulls soar overhead. The atmosphere is calm and tranquil, evoking a sense of peace."

### Use Cases:
- 🔎 Reverse image search.
- ♿ Scene descriptions for the visually impaired.
- 📖 Story generation and content understanding.
- 🏷️ Dataset labeling for computer vision/ML tasks.

## 🧪 Testing
- Test the app with sample images in the `assets` folder.
- Check the `logs/logging.log` file for detailed logs of image processing, caption generation, and LLM responses.

## 📝 Notes
- Ensure your `GROQ_API_KEY` is valid for LLM access via Groq API.
- The BLIP-2 model may require significant memory; ensure your system has enough resources.
- Add `.env` to `.gitignore` to avoid exposing API keys.

## 🌟 Future Improvements
- Add support for multiple LLMs for comparison.
- Integrate real-time image preprocessing (e.g., resizing, cropping).
- Enhance UI with more interactive elements (e.g., download description as text).

## 🤝 Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests. Let’s make this project even better together! 🚀