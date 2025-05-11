# Llama Chat Application 🦙💬

Welcome to the **Llama Chat Application**, a sleek and modern web-based chat interface powered by Groq's Language Model! This project uses FastAPI to serve a responsive UI styled with Tailwind CSS, allowing users to interact with the Llama model seamlessly. 🚀

## 📋 Project Overview

This application provides a chat interface where users can send messages to the Llama model and receive responses in real-time. The UI is designed to resemble modern AI platforms like grok.com, featuring a dark theme, clean typography, and smooth animations. The backend leverages FastAPI for efficient routing, LangChain for interacting with the Llama model, and includes logging for debugging. 🛠️

### Key Features 🌟
- **Interactive Chat**: Send messages and get responses from the Llama model.
- **Modern UI**: Dark gradient theme with Tailwind CSS styling.
- **Smooth Animations**: Fade-in effects for messages and typing indicators.
- **Error Handling**: Displays errors gracefully in the UI.
- **Logging**: Logs server activity for debugging and monitoring.

## 📂 Project Structure

Here's the directory structure of the project:

```
project/
├── log/                   # Directory for log files 📜
│   └── app.log
├── static/                # Static files (JavaScript) 📁
│   └── script.js
├── templates/             # HTML templates 📄
│   └── index.html
├── main.py               # FastAPI application code 🐍
├── requirements.txt      # Python dependencies 📦
└── .env                  # Environment variables 🔑
```

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites
- **Python 3.9+**: Ensure Python is installed. 🐍
- **pip**: Python package manager.
- **Groq API Key**: You'll need an API key from Groq to use the Llama model. 🔑

### 1. Clone the Repository 📥
Clone this project to your local machine:
```bash
git clone <repository-url>
cd project
```

### 2. Set Up a Virtual Environment 🌐
Create and activate a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies 📦
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
```
fastapi==0.111.0
uvicorn==0.30.1
langchain-groq==0.1.5
python-multipart==0.0.9
jinja2==3.1.4
starlette==0.37.2
markupsafe==2.1.5
python-dotenv==1.0.1
```

### 4. Configure Environment Variables 🔑
Create a `.env` file in the project root and add your Groq API key:
```
GROK_API_KEY=your_groq_api_key_here
```
Replace `your_groq_api_key_here` with your actual API key.

### 5. Run the Application 🚀
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
- The `--reload` flag enables auto-reloading during development.
- The server will run on `http://localhost:8000`.

## 🌐 Accessing the Application
Open your browser and navigate to:
```
http://localhost:8000
```
You'll see the chat interface with a heading in the top left, a welcome message, and an input area at the bottom to send messages to the Llama model. 🎉

## 💻 How It Works

### Backend (`main.py`) 🐍
- **FastAPI**: Handles routing and serves the web application.
  - `GET /`: Renders the homepage (`index.html`).
  - `POST /chat`: Processes user messages and returns Llama responses.
- **LangChain-Groq**: Interfaces with the Llama model (`meta-llama/llama-4-scout-17b-16e-instruct`).
- **Logging**: Logs server activity to `log/app.log` and the console for debugging.

### Frontend (`index.html` & `script.js`) 🌟
- **HTML Template (`index.html`)**:
  - Styled with Tailwind CSS for a modern, dark-themed UI.
  - Features a gradient header, chat area, and input form.
  - Includes animations (fade-in, typing indicator) for a polished look.
- **JavaScript (`script.js`)**:
  - Handles form submission, sends messages to the `/chat` endpoint, and displays responses dynamically.
  - Manages chat bubbles (user messages in blue, bot responses in gray, errors in red).

### Chat Flow 🔄
1. User types a message in the input field and submits the form.
2. JavaScript (`script.js`) sends the message to the `/chat` endpoint via a POST request.
3. FastAPI processes the message, sends it to the Llama model, and returns the response.
4. The response is appended to the chat area as a bot message.

## 🎨 UI Details

The UI is designed to be clean and user-friendly, inspired by modern AI platforms:
- **Header**: Gradient background (indigo to purple) with the app title and status indicator.
- **Chat Area**: White background with rounded corners, a custom scrollbar, and centered welcome message.
- **Input Form**: Positioned at the bottom, with a text input and a "Send" button featuring an arrow icon.
- **Animations**:
  - **Fade-In**: Messages fade in smoothly.
  - **Typing Indicator**: Animated dots while waiting for a response (though currently static in the UI).

## 🐛 Debugging & Logs

- **Logs**: Check `log/app.log` for server activity, errors, and debugging information.
- **Browser Console**: Open the browser's developer tools (F12 > Console) to debug JavaScript errors.

Example log entry:
```
2025-05-11 12:00:00,000 - main - INFO - Successfully processed message: Hello
```

## 🔧 Potential Improvements

- **Memory**: Add conversation history to maintain context across messages.
- **Persistent Storage**: Use a database to store chat history.
- **Authentication**: Add user authentication for personalized chats.
- **Themes**: Allow users to switch between light and dark themes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq**: For providing the Llama model and API.
- **FastAPI**: For the amazing web framework.
- **Tailwind CSS**: For the utility-first CSS framework.

---

Happy chatting with Llama! If you have any questions or need help, feel free to reach out. 💬✨