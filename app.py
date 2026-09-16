import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 AI Language Translation Tool")
st.write("Translate text between different languages using AI-powered translation.")

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

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

text = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here..."
)

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation completed!")
            st.text_area("Translated Text", translated, height=150)

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")