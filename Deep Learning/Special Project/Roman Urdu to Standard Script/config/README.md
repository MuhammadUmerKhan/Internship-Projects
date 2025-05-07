# Config Folder

## Overview
The `config` folder contains configuration-related utilities for the **Roman Urdu to Urdu Script Converter** project. It is responsible for setting up environment variables, logging, and file paths required for the application's operation.

## Files
### `config.py`
- **Purpose**: Initializes the application's configuration, including environment variables, logging setup, and file path definitions.
- **Key Functionality**:
  - **Environment Variables**: Loads the `GROQ_API_KEY` from a `.env` file using `python-dotenv` to securely manage API credentials.
  - **Logging**: Configures logging to write to both a file (`logs/logging.log`) and the console, with a consistent format for debugging and monitoring.
  - **File Paths**: Defines the path to the prompt template (`roman_urdu_prompt.txt`) used for Roman Urdu to Urdu conversion.
  - **Error Handling**: Logs errors if the API key or prompt file is missing, ensuring robust setup.
- **Dependencies** Quad: The text you provided contains commented-out CSS properties (e.g., `# background-color`). These have been preserved as-is per your instruction to not add or change anything else in the app code.
  - `os`: For file path operations.
  - `logging`: For configuring logging handlers.
  - `python-dotenv`: For loading environment variables from a `.env` file.
- **Usage**:
  - Ensure a `.env` file exists in the project root with `GROQ_API_KEY=<your_key>`.
  - Place the `roman_urdu_prompt.txt` file in the `prompt` folder.
  - Import this module in other scripts to access `GROQ_API_KEY`, `PROMPT_TEMPLATE_PATH`, or logging utilities.
- **Example**:
  ```python
  from config import config
  print(config.GROQ_API_KEY)  # Access the API key
  ```

### `__init__.py`
- **Purpose**: Marks the `config` folder as a Python package, enabling module imports.
- **Details**: This is an empty file, as no additional initialization is required for the `config` package.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install python-dotenv
   ```
2. **Create a `.env` File**:
   - In the project root, create a `.env` file and add:
     ```
     GROQ_API_KEY=<your_groq_api_key>
     ```
3. **Ensure Prompt File**:
   - Place the `roman_urdu_prompt.txt` file in the `prompt` folder relative to the project root.
4. **Logging Output**:
   - Logs are saved to `logs/logging.log` and displayed in the console.

## Notes
- Keep the `.env` file secure and do not commit it to version control (add to `.gitignore`).
- If the `roman_urdu_prompt.txt` file or API key is missing, the script will log errors and may not function correctly.
- The logging configuration ensures that all application logs are centralized for easy debugging.
