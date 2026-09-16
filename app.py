import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

# Title
st.title("🌐 AI Language Translation Tool")
st.write(
    "Translate text between different languages using an AI-powered translation service."
)

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

# Language selection
source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# Text input
text = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here...",
    height=150
)

# Translate button
if st.button("🔄 Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    elif source == target:
        st.info("ℹ️ Source and target languages are the same.")
        st.text_area(
            "Translated Text",
            text,
            height=150

            