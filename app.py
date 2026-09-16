import requests
import gradio as gr


def translate_text(text, source_lang, target_lang):
    if not text.strip():
        return "Please enter some text to translate."

    if source_lang == target_lang:
        return text

    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("responseStatus") == 200:
            return data["responseData"]["translatedText"]

        return "Translation failed. Please try again."

    except Exception as e:
        return f"Error: {str(e)}"


languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh"
}


def translate_from_dropdown(text, source, target):
    return translate_text(
        text,
        languages[source],
        languages[target]
    )


with gr.Blocks(title="AI Language Translation Tool") as app:

    gr.Markdown(
        """
        # 🌍 AI Language Translation Tool

        ### Translate text instantly between multiple languages

        This application uses a translation API to convert text
        from one language to another.
        """
    )

    with gr.Row():

        with gr.Column():
            source_language = gr.Dropdown(
                choices=list(languages.keys()),
                value="English",
                label="🌐 Source Language"
            )

            input_text = gr.Textbox(
                label="📝 Enter Text",
                placeholder="Type the text you want to translate...",
                lines=8
            )

        with gr.Column():
            target_language = gr.Dropdown(
                choices=list(languages.keys()),
                value="Hindi",
                label="🌐 Target Language"
            )

            output_text = gr.Textbox(
                label="✅ Translated Text",
                lines=8
            )

    with gr.Row():

        translate_button = gr.Button(
            "🔄 Translate",
            variant="primary"
        )

        clear_button = gr.Button(
            "🗑️ Clear"
        )

    translate_button.click(
        fn=translate_from_dropdown,
        inputs=[
            input_text,
            source_language,
            target_language
        ],
        outputs=output_text
    )

    clear_button.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[input_text, output_text]
    )

    gr.Markdown(
        """
        ---
        ### ✨ Features

        - 🌐 Multiple language support
        - ⚡ API-based translation
        - 📝 Easy text input
        - 🔄 Instant translation
        - 🗑️ Clear button
        - 💻 User-friendly interface

        **Developed as part of the CodeAlpha Artificial Intelligence Internship.**
        """
    )


if __name__ == "__main__":
    app.launch()