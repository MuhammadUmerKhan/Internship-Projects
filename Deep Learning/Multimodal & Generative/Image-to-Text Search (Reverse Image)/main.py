import streamlit as st
from PIL import Image
from app.chat_model import get_scene_description

# Set page configuration
st.set_page_config(page_title="Image-to-Text Search", page_icon="🖼️", layout="wide")

# Custom CSS Styling with Enhanced Visuals
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            # background: linear-gradient(135deg, #1e3c72, #2a5298);
            # color: #ecf0f1;
        }

        /* Title Styling */
        .main-title {
            font-size: 48px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            animation: fadeIn 1s ease-in;
        }

        /* Subtitle Styling */
        .subtitle {
            font-size: 22px;
            color: #bdc3c7;
            text-align: center;
            margin-bottom: 30px;
            font-style: italic;
        }

        /* Section Titles */
        .section-title {
            font-size: 28px;
            color: #ffffff;
            margin-top: 40px;
            text-align: left;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
            animation: slideIn 1s ease-out;
        }

        /* Description Text */
        .description {
            font-size: 18px;
            color: #ecf0f1;
            line-height: 1.8;
            background: rgba(0, 0, 0, 0.2);
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
        }

        /* Emoji Styling */
        .emoji {
            font-size: 28px;
            margin-right: 10px;
            vertical-align: middle;
        }

        /* Image Container */
        .stImage {
            border: 2px solid #3498db;
            border-radius: 10px;
            padding: 10px;
            background: rgba(255, 255, 255, 0.1);
        }

        /* Spinner Customization */
        .stSpinner {
            color: #3498db;
            font-size: 20px;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="main-title">🖼️ Image-to-Text Search | Scene Understanding with LLMs 🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert any uploaded image into a professionally written scene description using BLIP-2 + Qwen</div>', unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["📖 Project Overview", "📷 Upload Image"])

# --- Tab 1: Project Introduction ---
with tab1:
    st.markdown('<div class="section-title">🚀 Project Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="description">
        This project transforms visual content into human-readable, richly detailed scene descriptions.
        It's designed for reverse image search, storytelling, content understanding, and more.
        <br><br>
        <span class="emoji">🧠</span> <b>How It Works:</b><br>
        • The image is first processed using <b>BLIP-2</b> to extract a base caption.  
        • Then, a powerful <b>LLM (Qwen via Groq API)</b> turns that into a refined scene description.  
        • Outputs include landscape features, mood, objects, and contextual setting.
        <br><br>
        <span class="emoji">🧰</span> <b>Tech Stack:</b><br>
        • Vision Model: BLIP-2 (Salesforce)<br>
        • LLM Model: Qwen (Groq API)<br>
        • UI: Streamlit + CSS Styling<br>
        • Logging + Clean Modular Code
        <br><br>
        <span class="emoji">🌟</span> <b>Key Features:</b><br>
        • Upload any image for semantic scene understanding<br>
        • Supports highly detailed natural language generation<br>
        • Professional formatting & emoji support<br>
        • Real-time local inference + LLM refinement
        <br><br>
        <span class="emoji">🎯</span> <b>Use Cases:</b><br>
        • Reverse Image Search<br>
        • Scene Description for Visually Impaired<br>
        • Story Generation / Content Understanding<br>
        • Dataset Labeling for CV/ML
    </div>
    """, unsafe_allow_html=True)

# --- Tab 2: Image Upload & Result ---
with tab2:
    st.markdown('<div class="section-title">📷 Upload an Image</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=600, output_format="auto")

        with st.spinner("Generating scene description..."):
            description, caption = get_scene_description(uploaded_file)
        
        st.markdown('<div class="section-title">📝 Scene Caption</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='description'>{str(caption).capitalize()}.</div>", unsafe_allow_html=True)
        
        st.markdown('<div class="section-title">📝 Scene Description</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='description'>{description}</div>", unsafe_allow_html=True)