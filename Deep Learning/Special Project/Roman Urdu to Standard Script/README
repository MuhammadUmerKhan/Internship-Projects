# Roman to Native Script Converter 📝

![img](https://www.oneskyapp.com/blog/wp-content/uploads/sites/4/2023/07/unnamed-2.png)

## Overview 🌟
The **Roman to Native Script Converter** is an AI-powered web application designed to convert Romanized text from any language spoken in the world into its standardized, grammatically correct native script. Romanized Hindi and Urdu are specifically converted to Urdu script, while other languages are converted to their original scripts (e.g., Romanized Arabic to Arabic script, Romanized Chinese to Chinese characters). Built with a modern tech stack, it leverages advanced language models to ensure accurate and fluent translations, making it ideal for standardizing multilingual communication. The project features a user-friendly Streamlit interface with options for direct text input and file-based conversions.

## Features ✨
- **Text Conversion** 📜: Converts Romanized text in any language to its native script instantly via a web interface (e.g., "aap kaise ho?" to Urdu script, "ni hao" to Chinese characters).
- **File Conversion** 📂: Uploads `.txt` files containing Romanized text and downloads translated native script as `.txt` files.
- **AI-Powered Translation** 🤖: Uses the Qwen-QWQ-32B model (via GroqCloud) for precise, context-aware translations.
- **Noise Handling** 🧹: Corrects inconsistent spellings, slang, and repetitions for polished output.
- **Unrecognizable Input Handling** 🚫: Politely handles invalid inputs (e.g., "wrnefi") with a message: "Apologies, the text cannot be processed due to unrecognizable input."
- **Professional UI** 🎨: Streamlit-based interface with responsive design, custom styling, and intuitive navigation.
- **Logging** 📊: Comprehensive logging for debugging and monitoring conversion processes.
- **Secure Configuration** 🔐: Manages API keys securely using environment variables.

## Project Structure 📁
The project is organized into the following folders and key files:

### `config/` 🛠️
- **Purpose**: Handles configuration setup, including environment variables, logging, and file paths.
- **Files**:
  - `config.py`: Loads `GROQ_API_KEY` from `.env`, configures logging, and defines the path to `roman_prompt.txt`.
  - `__init__.py`: Marks the folder as a Python package.

### `converter/` 🔤
- **Purpose**: Contains the core logic for Romanized text to native script conversion.
- **Files**:
  - `converter.py`: Implements the `convert_text` function, using the Qwen-QWQ-32B model to translate text, with robust prompt engineering and response cleaning. Now supports global languages and handles unrecognizable inputs.
  - `__init__.py`: Marks the folder as a Python package.

### `utils/` 🧰
- **Purpose**: Provides utility functions for configuring the language model.
- **Files**:
  - `utils.py`: Defines `configure_llm` to initialize the `ChatGroq` model with the Groq API.
  - `__init__.py`: Marks the folder as a Python package.

### `app.py` 🌐
- **Purpose**: Implements the Streamlit web application with three tabs:
  - **Introduction**: Describes the project, its purpose, and tech stack.
  - **Translator**: Allows users to input Romanized text in any language and view the translated native script (e.g., Urdu script for Hindi/Urdu, Chinese characters for Chinese).
  - **File Converter**: Supports uploading Romanized text `.txt` files, viewing/editing translated script, and downloading as `.txt`. Updated to ensure translated text is not bold, matching the Translator tab.
- **Details**: Features custom CSS for styling, a sidebar with usage instructions, and error handling for a robust user experience.

### Other Files/Folders 📋
- **`prompt/`** (implied): Expected to contain `roman_prompt.txt` for the conversion prompt (not provided but referenced in `config.py`).
- **`logs/`** (generated): Stores log files (`logging.log`) for debugging and monitoring.

## Setup Instructions 🚀
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd roman-to-native-script-converter
   ```
2. **Install Dependencies**:
   ```bash
   pip install streamlit langchain langchain-groq python-dotenv
   ```
3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```
     GROQ_API_KEY=<your_groq_api_key>
     ```
   - Obtain a Groq API key from [GroqCloud](https://console.groq.com/keys).
4. **Prepare Prompt File**:
   - Create a `prompt` folder in the project root.
   - Add `roman_prompt.txt` (if required by your LLM setup) in `prompt/`.
5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   - Access the app at `http://localhost:8501` in your browser.

## Usage 📖
1. **Translator Tab** 🌐:
   - Navigate to the **Translator** tab.
   - Enter Romanized text (e.g., "aap kese ho?" for Urdu/Hindi, "ni hao" for Chinese) in the input box.
   - Click **Translate Now 🚀** to view the native script output (e.g., "آپ کیسے ہو؟" for Urdu/Hindi, "你好" for Chinese).
2. **File Converter Tab** 📂:
   - Navigate to the **File Converter** tab.
   - Upload a `.txt` file containing Romanized text.
   - Click **Convert File 🚀** to process the file.
   - View and edit the translated script, then download as `translated_script.txt`.
3. **View Logs** 📊:
   - Check `logs/logging.log` for conversion details or errors.

## Example 📝
- **Input (Romanized Text)**:
  - "mujhe kal ek dost se milna hai" (Romanized Urdu/Hindi)
  - "ni hao" (Romanized Chinese)
  - "wrnefihweilfenfwbelfbefbqf" (Unrecognizable)
- **Output (Native Script)**:
  - "مجھے کل ایک دوست سے ملنا ہے" (Urdu script)
  - "你好" (Chinese characters)
  - "Apologies, the text cannot be processed due to unrecognizable input"
- **File Input**: Upload `sample_roman_text.txt` with content like:
  ```
  salaam, aap kese hain?
  ni hao ma?
  ```
- **File Output**: Download `translated_script.txt` with:
  ```
  سلام، آپ کیسے ہیں؟
  你好吗？
  ```

## Tech Stack 🖥️
- **AI Model**: Qwen-QWQ-32B (via GroqCloud) 🤖
- **Frameworks**: Python, LangChain, Streamlit 🐍
- **Libraries**: `langchain-groq`, `python-dotenv`, `streamlit` 📚
- **Features**: Regex preprocessing, prompt engineering, logging, file I/O 📊

## Notes 📌
- **Security**: Keep the `.env` file secure and add it to `.gitignore` to prevent exposing the `GROQ_API_KEY`.
- **Prompt File**: If `roman_prompt.txt` is required, ensure it exists in `prompt/` or adjust `config.py` accordingly.
- **Logging**: Logs in `logs/logging.log` help diagnose issues with LLM configuration, conversions, or file processing.
- **Error Handling**: The app includes robust error handling for invalid inputs, missing files, or API issues, with user-friendly error messages.
- **Scalability**: The modular structure (`config`, `converter`, `utils`) supports easy extension, such as adding new models or features.

## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License 📜
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments ❤️
- Powered by **GroqCloud** and **Streamlit** 🌟.