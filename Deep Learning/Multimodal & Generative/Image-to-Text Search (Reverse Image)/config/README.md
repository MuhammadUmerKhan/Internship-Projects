# Config Folder Overview

The `config` folder contains configuration settings and utilities for managing environment variables and initializing the language model (LLM) used in the Image-to-Text Search application. It ensures secure handling of API keys and proper logging setup.

## Files in This Folder

### 1. `__init__.py`
- **Purpose**: Marks the `config` directory as a Python package, enabling imports from this folder.
- **Details**: Currently empty, but allows for future initialization logic if needed.

### 2. `config.py`
- **Purpose**: Manages application configuration, including environment variable loading and LLM initialization.
- **Key Features**:
  - Loads environment variables (e.g., `GROK_API_KEY`) from a `.env` file using `python-dotenv`.
  - Sets up logging to both a file (`logs/logging.log`) and the console.
  - Initializes the LLM (e.g., `qwen-qwq-32b`) using utilities from the `utils` module.
- **Dependencies**: Requires `os`, `logging`, `dotenv`, and `utils.utils`.
- **Logging**: Saves logs to `logs/logging.log` and outputs to the console, with error handling for missing API keys or LLM configuration issues.

## Usage
1. Create a `.env` file in the root directory with the following format:
   ```
   GROK_API_KEY=your_api_key_here
   ```
2. Ensure all dependencies are installed (see `requirements.txt` in the root directory), including `python-dotenv`.
3. Import and use the configuration in other modules, e.g., `from config import config` (though direct imports are not needed as the file sets global configurations).