# Templates Folder 📄✨

Welcome to the `templates` folder of the Llama Chat Application! This directory contains the HTML templates used by FastAPI to render the web interface. Below, you'll find a detailed overview of its contents and purpose.

## 📋 Purpose

The `templates` folder stores the HTML files that define the structure and layout of the application's user interface. These templates are rendered by FastAPI using the Jinja2 templating engine, allowing dynamic content to be injected into the HTML (e.g., chat messages).

## 📂 Folder Structure

```
templates/
└── index.html    # Main HTML template for the chat interface
```

Currently, this folder contains a single file, `index.html`, which serves as the primary template for the application.

## 📜 File Overview: `index.html`

### Purpose
The `index.html` file is the core template for the Llama Chat Application's web interface. It defines the layout, styling, and behavior of the chat UI, including the header, chat area, input form, and footer.

### Key Features 🌟
- **Modern UI**: Styled with Tailwind CSS, featuring a dark gradient theme inspired by platforms like grok.com.
- **Dynamic Rendering**: Uses Jinja2 to render chat messages dynamically (though currently static in this version).
- **Responsive Design**: Adapts to different screen sizes with a mobile-friendly layout.
- **Animations**: Includes fade-in effects for chat messages and a typing indicator animation (though the latter is static in this version).
- **Custom Scrollbar**: Styled scrollbar for the chat area to match the UI theme.

### Structure of `index.html`
- **Head Section**:
  - Imports Tailwind CSS via CDN for styling.
  - Loads the Inter font from Google Fonts for clean typography.
  - Defines custom Tailwind colors (e.g., `primary` shades).
  - Includes CSS for animations (fade-in, typing indicator) and a custom scrollbar.
- **Body Section**:
  - **Header**: Gradient background (indigo to purple) with the app title, a chat icon, and a status indicator.
  - **Main Content**: Chat area with a welcome message and placeholder for chat messages.
  - **Form**: Input field and "Send" button at the bottom for user messages.
  - **Footer**: Simple footer with a copyright notice.
  - **Scripts**: Links to `script.js` for handling form submission and chat functionality.

### Styling Details 🎨
- **Background**: Light gray (`bg-gray-100`) for the body, with a white chat area (`bg-white`).
- **Chat Area**: Rounded corners, shadow, and a custom scrollbar (`scrollbar-custom` class).
- **Input Form**: Bordered input with focus effects (`focus:ring-indigo-500`) and a gradient "Send" button.
- **Animations**:
  - **Fade-In**: Applied to chat messages via the `chat-bubble` class.
  - **Typing Indicator**: Animated dots (currently static but styled with CSS).

## 🛠️ Usage

### Rendering with FastAPI
The `index.html` template is rendered by the FastAPI application in `main.py`:
- **GET `/`**: The root endpoint renders `index.html` with an empty `messages` list.
- **Dynamic Content**: The template is designed to accept a `messages` list for displaying chat history (though this feature is not yet implemented in this version).

### Integration with JavaScript
The template works with `static/script.js` to handle user interactions:
- The form (`id="chatForm"`) submits messages to the `/chat` endpoint.
- JavaScript dynamically appends user messages and bot responses to the chat area (`id="chatBox"`).

### Customization
To modify the UI:
1. **Change Styling**: Edit the Tailwind classes or custom CSS in the `<style>` section.
2. **Update Layout**: Adjust the HTML structure (e.g., reposition the input form).
3. **Add Features**: Extend the template to support new features like displaying chat history.

## 📝 Notes
- **Chat History**: This version does not yet store or display chat history. See the main README for potential improvements like adding memory.
- **Dependencies**: Ensure Tailwind CSS CDN and Inter font are accessible, as they are loaded externally.
- **Animations**: The typing indicator is styled but not functional in this version; it requires JavaScript updates to animate during response loading.

## 🔗 Related Files
- **../main.py**: Renders this template using FastAPI and Jinja2.
- **../static/script.js**: Handles client-side logic for form submission and chat updates.

---

This README provides a focused guide for the `templates` folder. For more details on the overall project, check the main `README.md` in the project root! 🚀