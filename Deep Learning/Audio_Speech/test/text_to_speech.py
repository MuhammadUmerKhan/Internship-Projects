import streamlit as st
from gtts import gTTS
import os
import tempfile

def text_to_speech_gtts(text, language='en', slow=False):
    """
    Convert text to speech using gTTS and return the MP3 file path.
    
    Args:
        text (str): Text to convert to speech.
        language (str): Language code (default: 'en' for English).
        slow (bool): Slow speech if True (default: False).
    
    Returns:
        str: Path to the generated MP3 file, or None if an error occurs.
    """
    if not text or not isinstance(text, str):
        st.error("Please enter valid text.")
        return None
    
    try:
        # Create a temporary file for the MP3
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            filename = tmp_file.name
        
        # Generate MP3 with gTTS
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(filename)
        
        if not os.path.exists(filename):
            st.error("Failed to generate audio file.")
            return None
        
        return filename
    
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

# Streamlit app
st.set_page_config(page_title="Text-to-Speech Converter", page_icon="🎙️", layout="centered")

st.title("Text-to-Speech Converter")
st.markdown("""
    Enter text below and click **Listen** to hear it as speech. 
    You can also download the audio as an MP3 file.
""")

# Text input
user_text = st.text_area(
    "Enter your text here:",
    placeholder="Type something to convert to speech...",
    height=150
)

# Language selection
language = st.selectbox(
    "Select Language",
    options=[("English", "en"), ("French", "fr"), ("Spanish", "es")],
    format_func=lambda x: x[0],
    index=0
)

# Speed toggle
slow = st.checkbox("Slow Speech", value=False)

# Listen button
if st.button("Listen", key="listen_button", help="Generate and play the audio"):
    if user_text:
        with st.spinner("Generating audio..."):
            mp3_file = text_to_speech_gtts(user_text, language=language[1], slow=slow)
            if mp3_file:
                # Play audio in browser
                st.audio(mp3_file, format="audio/mp3")
                st.success("Audio generated successfully!")
                
                # Provide download button
                with open(mp3_file, "rb") as file:
                    st.download_button(
                        label="Download MP3",
                        data=file,
                        file_name="output.mp3",
                        mime="audio/mpeg",
                        key="download_button"
                    )
                
                # Clean up temporary file
                try:
                    os.unlink(mp3_file)
                except Exception:
                    pass
    else:
        st.error("Please enter some text to convert.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>
        Built with Streamlit and gTTS for internship project | © 2025
    </p>
""", unsafe_allow_html=True)