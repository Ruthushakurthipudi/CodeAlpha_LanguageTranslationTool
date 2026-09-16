import streamlit as st
import requests

st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 AI Language Translation Tool")

st.write(
    "Translate text between different languages using an online translation API."
)

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

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

text = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here...",
    height=150
)

if st.button("🔄 Translate"):

    if not text.strip():
        st.warning("⚠️ Please enter some text.")

    elif source == target:
        st.info("Source and target languages are the same.")
        st.text_area(
            "Translated Text",
            text,
            height=150
        )

    else:
        try:
            url = "https://api.mymemory.translated.net/get"

            params = {
                "q": text,
                "langpair": f"{languages[source]}|{languages[target]}"
            }

            response = requests.get(
                url,
                params=params,
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            translated_text = data["responseData"]["translatedText"]

            st.success("✅ Translation completed!")

            st.text_area(
                "Translated Text",
                translated_text,
                height=150
            )

        except Exception as e:
            st.error("❌ Translation failed.")
            st.write(f"Error: {e}")