import streamlit as st
import os
from tts_engine import TTSEngine
from config import SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE, DEFAULT_SLOW

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "page" not in st.session_state:
    st.session_state.page = "home"

# In-page CSS for attractive, non-white UI
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        # background-color: #2c3e50;
        # color: #ecf0f1;
    }
    
    /* Containers */
    .stTextArea textarea, .stSelectbox, .stCheckbox {
        background-color: #34495e;
        color: #ecf0f1;
        border: 2px solid #3498db;
        border-radius: 8px;
        padding: 10px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #3498db;
        color: #ecf0f1;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    
    /* Download button */
    .stDownloadButton>button {
        background-color: #27ae60;
        color: #ecf0f1;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 14px;
    }
    .stDownloadButton>button:hover {
        background-color: #219653;
    }
    
    /* Headers and text */
    h1, h2, h3 {
        color: #3498db;
        text-align: center;
    }
    p, li {
        color: #ecf0f1;
        font-size: 16px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #34495e;
    }
    
    /* Expander */
    .stExpander {
        background-color: #34495e;
        border: 1px solid #3498db;
        border-radius: 8px;
    }
    
    /* Error and success messages */
    .stAlert {
        background-color: #e74c3c;  /* Error */
        color: #ecf0f1;
        border-radius: 8px;
    }
    .stSuccess {
        background-color: #27ae60;  /* Success */
        color: #ecf0f1;
        border-radius: 8px;
    }
    
    /* Footer */
    hr {
        border-color: #3498db;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app configuration
# st.set_page_config(
#     page_title="TTS Converter 🎙️",
#     page_icon="🎙️",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# Sidebar with How to Use
with st.sidebar:
    st.header("How to Use 📖")
    st.markdown("""
        Welcome to the TTS Converter! Follow these steps to turn text into speech:

        1. **Visit the Converter**: Click "Go to Converter" on the home page. 🏠
        2. **Enter Text**: Type or paste your text in the provided box. 📝
        3. **Choose Options**: Select a language and speed (slow or normal). 🌐
        4. **Listen**: Click the **Listen** button to hear your text as audio. 🔊
        5. **Download**: Save the audio as an MP3 file if needed. 💾
        6. **Check History**: View recent conversions below the input area. 📜
    """)

# Page navigation
def show_home_page():
    """Display the home page with welcome message."""
    st.title("Welcome to TTS Converter 🎙️")
    st.markdown("""
        Transform your text into high-quality speech with ease! 🚀  
        This app uses advanced text-to-speech technology to convert your input into audio, 
        with support for multiple languages and customizable speed. Perfect for presentations, 
        learning, or creative projects! 🌟

        **Ready to start?** Click below to access the converter. 👇
    """)
    if st.button("Go to Converter 🛠️", key="go_converter"):
        st.session_state.page = "converter"

def show_converter_page():
    """Display the TTS converter page."""
    st.title("Text-to-Speech Converter 🔊")
    st.markdown("""
        Enter your text below, choose your settings, and click **Listen** to hear the audio! 🎵  
        You can also download the MP3 or view recent conversions. 📚
    """)

    # Text input
    user_text = st.text_area(
        "Your Text 📝:",
        placeholder="Type something to convert to speech...",
        height=150,
        key="text_input"
    )

    # Language and speed controls
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox(
            "Language 🌐",
            options=SUPPORTED_LANGUAGES,
            format_func=lambda x: x[0],
            index=[x[1] for x in SUPPORTED_LANGUAGES].index(DEFAULT_LANGUAGE)
        )
    with col2:
        slow = st.checkbox("Slow Speech 🐢", value=DEFAULT_SLOW)

    # Listen button
    if st.button("Listen 🎧", key="listen_button", help="Generate and play audio"):
        if user_text:
            with st.spinner("Generating audio... ⏳"):
                tts_engine = TTSEngine(language=language[1], slow=slow)
                mp3_file = tts_engine.convert_to_speech(user_text)
                
                if mp3_file:
                    st.audio(mp3_file, format="audio/mp3")
                    st.success("Audio generated successfully! 🎉")
                    
                    # Add to history
                    st.session_state.history.append({
                        "text": user_text[:50] + ("..." if len(user_text) > 50 else ""),
                        "language": language[0],
                        "slow": slow,
                        "mp3_file": mp3_file
                    })
                    
                    # Download button
                    with open(mp3_file, "rb") as file:
                        st.download_button(
                            label="Download MP3 💾",
                            data=file,
                            file_name="output.mp3",
                            mime="audio/mpeg",
                            key=f"download_{len(st.session_state.history)}"
                        )
                else:
                    st.error("Failed to generate audio. Check logs for details. 😔")
        else:
            st.error("Please enter some text. 😞")

    # History section
    if st.session_state.history:
        st.subheader("Recent Conversions 📜")
        for i, entry in enumerate(st.session_state.history):
            with st.expander(f"Conversion {i+1}: {entry['text']}"):
                st.write(f"**Language**: {entry['language']} 🌐")
                st.write(f"**Slow Speech**: {'Yes' if entry['slow'] else 'No'} 🐢")
                st.audio(entry['mp3_file'], format="audio/mp3")
                with open(entry['mp3_file'], "rb") as file:
                    st.download_button(
                        label="Download MP3 💾",
                        data=file,
                        file_name=f"output_{i+1}.mp3",
                        mime="audio/mpeg",
                        key=f"download_history_{i}"
                    )

    # Footer
    st.markdown("""
        <hr>
        <p style='text-align: center; color: #ecf0f1;'>
            Built with ❤️ using Streamlit & gTTS
        </p>
    """, unsafe_allow_html=True)

# Page routing
if st.session_state.page == "home":
    show_home_page()
else:
    show_converter_page()

# Cleanup temporary files
def cleanup():
    for entry in st.session_state.history:
        try:
            os.unlink(entry['mp3_file'])
        except Exception:
            pass

import atexit
atexit.register(cleanup)