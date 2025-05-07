# Converter Folder

## Overview
The `converter` folder contains the core logic for converting Roman Urdu text to standardized Urdu script in the **Roman Urdu to Urdu Script Converter** project. It implements the translation functionality using a language model and handles text processing and logging.

## Files
### `converter.py`
- **Purpose**: Defines the main function for converting Roman Urdu to Urdu script and manages logging for the conversion process.
- **Key Functionality**:
  - **Text Conversion**: The `convert_text` function takes Roman Urdu input, processes it using a language model (Qwen-QWQ-32B), and returns the translated Urdu script.
  - **Prompt Engineering**: Uses a detailed prompt to guide the LLM to produce accurate, grammatically correct, and contextually appropriate Urdu output, handling noisy or informal input.
  - **Response Cleaning**: The `clean_response` function removes unnecessary tags (e.g., `<think>`) from the LLM's output.
  - **Logging**: Configures logging to write to `logs/logging.log` and the console, tracking conversion success and errors.
- **Dependencies**:
  - `os`: For file path operations.
  - `re`: For regular expression-based response cleaning.
  - `logging`: For logging conversion events.
  - `langchain.schema`: For structuring LLM messages (`SystemMessage`, `HumanMessage`).
  - `utils.utils`: For configuring the LLM (via `configure_llm`).
- **Usage**:
  - Import the `convert_text` function in other scripts (e.g., Streamlit app) to perform conversions.
  - Ensure the LLM is configured via `utils.configure_llm` and required dependencies are installed.
- **Example**:
  ```python
  from converter.converter import convert_text
  result = convert_text("aap kese ho?")
  print(result)  # Outputs: آپ کیسے ہیں؟
  ```

### `__init__.py`
- **Purpose**: Marks the `converter` folder as a Python package, enabling module imports.
- **Details**: This is an empty file, as no additional initialization is required for the `converter` package.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install langchain
   ```
   - Additional dependencies (e.g., for `utils.configure_llm`) may be required based on the LLM setup.
2. **Configure Logging**:
   - Logs are saved to `logs/logging.log` in the project directory.
   - Ensure the `logs` folder is writable.
3. **LLM Configuration**:
   - The `utils.configure_llm` function must be properly set up with access to the Qwen-QWQ-32B model (e.g., via Groq API).
   - Ensure the `GROQ_API_KEY` is set in the `.env` file (see `config` folder documentation).

## Notes
- The `convert_text` function is designed to handle noisy Roman Urdu input, such as inconsistent spellings or slang, and produce polished Urdu script.
- The logging configuration centralizes conversion logs for debugging and monitoring.
- Ensure the `utils` module is available and correctly configured to avoid runtime errors.