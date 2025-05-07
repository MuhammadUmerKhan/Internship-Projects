import streamlit as st
from converter.converter import convert_text
import io

# Page configuration
st.set_page_config(
    page_title="Roman to Native Script Converter",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main { background-color: #f5f7fa; }
    .stTextArea textarea { 
        border-radius: 8px; 
        border: 1px solid #e0e0e0; 
        # background-color: #f9f9f9;
        font-family: 'Noto Nastaliq Urdu', sans-serif;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #1e88e5;
        color: #ffffff;
        border-radius: 8px; 
        border: none;
        padding: 8px 16px;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #1565c0;
        color: #ffffff;
    }
    .header {
        # background-color: #e3f2fd;
        padding: 1rem;
        border-bottom: 1px solid #e0e0e0;
        # margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        color: #666;
        font-size: 0.9rem;
        margin-top: 2rem;
        border-top: 1px solid #e0e0e0;
    }
    .card {
        # background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    h1, h2, h3 {
        color: #1a237e;
        font-family: 'Roboto', sans-serif;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 500;
        color: #1a237e;
    }
    .stTabs [aria-selected="true"] {
        color: #1e88e5;
        border-bottom: 2px solid #1e88e5;
    }
    .translate-btn {
        display: flex;
        justify-content: center;
        margin: 1rem 0;
    }
    .stFileUploader label {
        color: #1a237e;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <h1>📝 Roman to Native Script Converter</h1>
    <p style="color: #666;">Convert Romanized Text to Its Native Script with AI 🚀</p>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ℹ️ <u>About</u>", unsafe_allow_html=True)
    st.markdown("""
    A smart tool to convert Romanized text in any language to its native script using advanced AI technology. 
    Romanized Hindi and Urdu are converted to Urdu script, while other languages are converted to their original scripts (e.g., Arabic to Arabic script, Chinese to Chinese characters). Powered by **Qwen-qwq-32B** via **GroqCloud** 🌟.
    """)
    st.markdown("### 📘 <u>How to Translate</u>", unsafe_allow_html=True)
    st.markdown("""
    Follow these steps to convert Romanized text to its native script:
    1. Go to the **Translator** tab 🌐.
    2. Enter your Romanized text in the input box ✍️ (e.g., "aap kese ho?" for Urdu/Hindi, "ni hao" for Chinese).
    3. Click the **Translate Now 🚀** button.
    4. View the converted native script in the output box ✅ (e.g., Urdu script for Hindi/Urdu, Chinese characters for Chinese).
    """)
    st.markdown("### 📂 <u>How to Use File Converter</u>", unsafe_allow_html=True)
    st.markdown("""
    1. Go to the **File Converter** tab 📂.
    2. Upload a `.txt` file containing Romanized text 📤.
    3. Click **Convert File 🚀** to translate.
    4. View and edit the translated script in the output box ✅, then download it as a `.txt` file 📥.
    """)

# Tabs
tab1, tab2, tab3 = st.tabs(["📖 Introduction", "🌐 Translator", "📂 File Converter"])

# Introduction Tab
with tab1:
    st.header("📚 About the Project")
    st.markdown("""
    Welcome to the **Roman to Native Script Converter**, a tool designed to bridge the gap between Romanized text and standardized native scripts for languages worldwide 🌉.

    ### 📌 Project Overview
    This app converts Romanized text from any language into its native script using a powerful language model 💡. Romanized Hindi and Urdu are converted to Urdu script, while other languages are converted to their original scripts (e.g., "aap kese ho?" to "آپ کیسے ہو؟" for Urdu/Hindi, "ni hao" to "你好" for Chinese).

    ### 🧠 How It Works
    - **Input:** Enter Romanized text in any language ✍️.
    - **Process:** Our AI, powered by Qwen-QWQ-32B, detects the language and converts the text to its native script 🤖 (Urdu script for Hindi/Urdu, original script for others).
    - **Output:** Receive accurate native script with proper formatting ✅.

    ### 🔧 Tech Stack
    - **AI Model:** Qwen-QWQ-32B (<a href="https://console.groq.com/">GroqCloud</a>) 🖥️
    - **Framework:** Python, LangChain, Streamlit 🐍
    - **Features:** Regex preprocessing, prompt engineering, logging 📊

    ### ✅ Why This Matters
    Romanized text is popular but inconsistent across languages. This tool:
    - Standardizes text into native scripts for formal use 📝
    - Preserves linguistic accuracy 🎯
    - Enhances multilingual communication 🌍
    """, unsafe_allow_html=True)

# Translator Tab
with tab2:
    st.header("Roman to Native Script Translator 🌟")
    st.markdown("Convert your Romanized text to its native script instantly! ⚡")

    # Input and Output columns
    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.subheader("✍️ Romanized Text Input")
        roman_input = st.text_area(
            "",
            height=100,
            placeholder="e.g., aap kese ho? (Urdu/Hindi), ni hao (Chinese)",
            key="roman_input"
        )

    # Translate button
    translate_clicked = st.button("**Translate Now** 🚀", use_container_width=True)

    with col2:
        st.subheader("✅ Native Script Output")
        if translate_clicked and roman_input:
            with st.spinner("Converting... ⏳"):
                try:
                    native_output = convert_text(roman_input)
                    st.text_area(
                        "",
                        value=native_output,
                        height=100,
                        key="native_output",
                        disabled=True
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)} 😓")
        else:
            st.text_area(
                "",
                height=100,
                placeholder="Translated native script will appear here... 👀",
                disabled=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# File Converter Tab
with tab3:
    st.header("Roman to Native Script File Converter 📂")
    st.markdown("Upload a Romanized text file and download the translated native script! 📤")

    # File uploader
    uploaded_file = st.file_uploader(
        "Upload a .txt file containing Romanized text 📤",
        type=["txt"],
        accept_multiple_files=False
    )

    if uploaded_file:
        # Read the file content
        file_content = uploaded_file.read().decode("utf-8")
        col1, col2 = st.columns([1, 1], gap="medium")

        with col1:
            st.subheader("📜 File Content (Romanized Text)")
            st.text_area(
                "",
                value=file_content,
                height=100,
                key="file_content",
                disabled=True
            )

        with col2:
            st.subheader("✅ Translated Native Script")
            if "translated_content" not in st.session_state:
                st.session_state.translated_content = ""
            translated_input = st.text_area(
                "",
                value=st.session_state.translated_content,
                height=100,
                key="translated_input"
            )
        
        col1, col2 = st.columns([1, 1], gap="small")
        with col1:
            # Convert button
            if st.button("**Convert File 🚀**", use_container_width=True):
                with st.spinner("Converting file... ⏳"):
                    try:
                        # Convert the file content
                        translated_content = convert_text(file_content)
                        st.session_state.translated_content = translated_content
                        st.success("File converted successfully! 🎉")
                    except Exception as e:
                        st.error(f"Error: {str(e)} 😓")
        with col2:
            # Download button (appears after conversion)
            if st.session_state.translated_content:
                translated_file = io.StringIO(st.session_state.translated_content)
                st.download_button(
                    label="**Download Translated Native Script 📥**",
                    data=st.session_state.translated_content,
                    file_name="translated_script.txt",
                    mime="text/plain",
                    use_container_width=True
                )

    else:
        st.info("Please upload a .txt file to start conversion. 👀")

# Footer
st.markdown("""
<div class="footer">
    Built with ❤️ | Powered by GroqCloud & Streamlit 🌟
</div>
""", unsafe_allow_html=True)