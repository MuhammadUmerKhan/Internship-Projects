# App Folder Overview

The `app` folder contains the core functionality for the Image-to-Text Search application. It handles image loading, caption generation, and scene description refinement using BLIP-2 and a language model (Qwen via Groq API). This folder is part of a Streamlit-based project that transforms images into detailed textual descriptions.

## Files in This Folder

### 1. `__init__.py`
- **Purpose**: Marks the `app` directory as a Python package, enabling imports from this folder.
- **Details**: Currently empty, but allows for future initialization logic if needed.

### 2. `img_opener.py`
- **Purpose**: Provides functionality to load images using the PIL library and logs the process.
- **Key Function**:
  - `load_image(uploaded_file)`: Opens an image file, logs success or failure, and returns a PIL Image object.
- **Logging**: Saves logs to `logs/logging.log` and outputs to the console.

### 3. `image_captioning.py`
- **Purpose**: Generates captions for images using the BLIP-2 model from Salesforce.
- **Key Function**:
  - `generate_caption(image)`: Takes a PIL Image object, processes it with BLIP-2, and returns a raw caption.
- **Dependencies**: Uses `transformers` for BLIP-2 (`BlipProcessor` and `BlipForConditionalGeneration`), `torch` for model inference, and `app.img_opener` for image loading.
- **Logging**: Saves logs to `logs/logging.log` and outputs to the console.

### 4. `chat_model.py`
- **Purpose**: Refines raw captions into detailed scene descriptions using a language model (Qwen via Groq API).
- **Key Functions**:
  - `generate_scene(caption)`: Takes a raw caption, enhances it using the LLM, and returns a refined description.
  - `get_scene_description(image_path)`: Orchestrates the process by loading an image, generating a caption, and refining it into a scene description.
- **Dependencies**: Uses `app.img_opener` for image loading, `app.image_captioning` for caption generation, `utils.utils` for LLM configuration, and `langchain_core` for message handling.
- **Logging**: Saves logs to `logs/logging.log` and outputs to the console.

### 5. `main.py`
- **Purpose**: The main Streamlit application that provides the user interface for uploading images and displaying scene descriptions.
- **Features**:
  - Displays a project overview and an image upload interface.
  - Uses custom CSS for styling, including gradients, animations, and responsive design.
  - Calls `get_scene_description` from `chat_model.py` to process uploaded images.
- **Dependencies**: Uses `PIL` for image handling and `app.chat_model` for scene description generation.

## Usage
1. Ensure all dependencies are installed (see `requirements.txt` in the root directory).
2. Run the Streamlit app using:
   ```bash
   streamlit run app/main.py
   ```
3. Upload an image via the UI to generate a detailed scene description.
