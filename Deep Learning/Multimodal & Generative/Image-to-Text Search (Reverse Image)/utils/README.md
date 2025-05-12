# Utils Folder Overview

The `utils` folder contains utility functions and configurations to support the Image-to-Text Search application. It provides tools for initializing and managing the language model (LLM) used in the project, along with logging mechanisms for tracking operations.

## Files in This Folder

### 1. `__init__.py`
- **Purpose**: Marks the `utils` directory as a Python package, enabling imports from this folder.
- **Details**: Currently empty, but allows for future initialization logic if needed.

### 2. `utils.py`
- **Purpose**: Provides utility functions for configuring and managing the LLM (e.g., Qwen via Groq API).
- **Key Function**:
  - `configure_llm(MODEL_NAME)`: Initializes a ChatGroq language model with a specified model name, using the API key from the `config` module. Returns the configured LLM instance or an error message if configuration fails.
- **Features**:
  - Sets a deterministic temperature of 0 for consistent responses.
  - Implements logging to both `logs/logging.log` and the console.
  - Handles exceptions and logs errors for debugging.
- **Dependencies**: Requires `os`, `logging`, `langchain_groq`, and `config.config`.

## Usage
1. Ensure all dependencies are installed (see `requirements.txt` in the root directory), including `langchain_groq`.
2. Import and use the utility function in other modules, e.g.:
   ```python
   from utils import utils
   llm = utils.configure_llm("qwen-qwq-32b")
   ```
3. Ensure the `GROQ_API_KEY` is set in the `.env` file and loaded via the `config` module.