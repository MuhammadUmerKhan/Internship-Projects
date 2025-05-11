# Static Folder 📁✨

Welcome to the `static` folder of the Llama Chat Application! This directory contains static files, such as JavaScript, that enhance the interactivity of the web interface. Below, you'll find a detailed overview of its contents and purpose.

## 📋 Purpose

The `static` folder stores static assets that are served directly by FastAPI to support the client-side functionality of the application. These files are not dynamically rendered like templates but are essential for handling user interactions and updating the UI in real-time.

## 📂 Folder Structure

```
static/
└── script.js    # JavaScript file for client-side logic
```

Currently, this folder contains a single file, `script.js`, which manages the chat functionality on the frontend.

## 📜 File Overview: `script.js`

### Purpose
The `script.js` file contains the JavaScript code that powers the interactive features of the Llama Chat Application. It handles form submission, communicates with the FastAPI backend, and dynamically updates the chat area with user messages and bot responses.

### Key Features 🌟
- **Form Submission**: Listens for submit events on the chat form (`id="chatForm"`) and prevents default behavior.
- **Message Handling**: Adds user messages to the chat area (`id="chatBox"`) as blue bubbles.
- **API Requests**: Sends messages to the `/chat` endpoint via a POST request and retrieves bot responses.
- **Response Display**: Appends bot responses as gray bubbles and errors as red bubbles.
- **Scroll Management**: Ensures the chat area scrolls to the latest message after each update.
- **Error Handling**: Displays errors gracefully if the API request fails.

### Code Breakdown
- **Event Listener**: Attaches to the form's `submit` event.
- **User Message**: Creates a `div` element with a blue background (`bg-blue-600`) for user input.
- **API Call**: Uses `fetch` to POST the message to `/chat` with URL-encoded data.
- **Bot Response**: Creates a `div` element with a gray background (`bg-gray-200`) for the bot's reply.
- **Error Handling**: Creates a `div` element with a red background (`bg-red-100`) for errors.
- **Scroll Behavior**: Updates `scrollTop` to keep the latest message in view.

### Integration
- **Dependency**: Works with `templates/index.html`, which includes `<script src="/static/script.js"></script>` to load this file.
- **Backend**: Relies on the `/chat` endpoint in `main.py` to process messages and return responses.

## 🛠️ Usage

### Serving Static Files
The `static` folder is mounted by FastAPI in `main.py` using:
```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```
This allows the application to serve `script.js` at the URL `/static/script.js`.

### Running the Application
1. Ensure the `static` folder is in the project root alongside `main.py`.
2. Start the FastAPI server with:
   ```bash
   uvicorn main:app --reload
   ```
3. Open `http://localhost:8000` in a browser to see the chat interface, where `script.js` handles interactions.

### Customization
To modify the behavior:
- **Update Logic**: Edit `script.js` to change how messages are handled or styled.
- **Add Features**: Extend the script to include new interactions (e.g., typing indicators).
- **Debugging**: Use the browser's developer tools (F12 > Console) to troubleshoot JavaScript errors.

## 📝 Notes
- **Dependencies**: Requires the FastAPI server to be running and the `/chat` endpoint to be functional.
- **Performance**: The script uses asynchronous `fetch` for non-blocking API calls.
- **Limitations**: Currently lacks support for conversation memory or persistent storage; this would require backend changes.

## 🔗 Related Files
- **../main.py**: Mounts the `static` folder and handles API requests.
- **../templates/index.html**: Includes the script and defines the chat area.

---

This README provides a focused guide for the `static` folder. For more details on the overall project, check the main `README.md` in the project root! 🚀