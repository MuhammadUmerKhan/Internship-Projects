# Utils Folder

## Overview
The `utils` folder contains utility functions for the **Roman Urdu to Urdu Script Converter** project. It primarily handles the configuration of the language model (LLM) used for text conversion, ensuring seamless integration with the Groq API.

## Files
### `utils.py`
- **Purpose**: Provides a utility function to configure the LLM for Roman Urdu to Urdu script conversion.
- **Key Functionality**:
  - **LLM Configuration**: The `configure_llm` function initializes a `ChatGroq` model (e.g., Qwen-QWQ-32B) using the Groq API, setting parameters like temperature and API key.
  - **Logging**: Configures logging to write to `logs/logging.log` and the console, tracking LLM configuration success or errors.
  - **Error Handling**: Catches and logs exceptions during LLM setup, returning an error message if configuration fails.
- **Dependencies**:
  - `os`: For file path operations.
  - `logging`: For logging configuration events.
  - `langchain_groq`: For the `ChatGroq` LLM interface.
  - `config.config`: For accessing `GROQ_API_KEY`.
- **Usage**:
  - Import the `configure_llm` function to initialize the LLM in other scripts (e.g., `converter.py`).
  - Pass the desired model name (e.g., "qwen-qwq-32b") as an argument.
- **Example**:
  ```python
  from utils import utils
  llm = utils.configure_llm(MODEL_NAME="qwen-qwq-32b")
  ```

### `__init__.py`
- **Purpose**: Marks the `utils` folder as a Python package, enabling module imports.
- **Details**: This is an empty file, as no additional initialization is required for the `utils` package.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install langchain-groq
   ```
2. **Configure Environment**:
   - Ensure the `GROQ_API_KEY` is set in the `.env` file in the project root (see `config` folder documentation).
   - Example `.env`:
     ```
     GROQ_API_KEY=<your_groq_api_key>
     ```
3. **Logging Output**:
   - Logs are saved to `logs/logging.log` in the project directory.
   - Ensure the `logs` folder is writable.

## Notes
- The `configure_llm` function is critical for initializing the LLM used in the conversion process, so ensure the Groq API key is valid.
- Logging helps diagnose issues with LLM configuration, such as invalid API keys or model names.
- The `langchain_groq` package must be installed and compatible with the specified model (e.g., Qwen-QWQ-32B).