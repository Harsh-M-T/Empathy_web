import gradio as gr
import asyncio
from app import speak_with_emotion, emotion_classifier

def generate_empathetic_speech(text: str):
    if not text or not text.strip():
        gr.Warning("Please enter some text.")
        return None

    try:
        output_file = "gradio_output.mp3"
        audio_path = asyncio.run(speak_with_emotion(text, output_file))
        return audio_path
    except Exception as e:
        gr.Error(f"An error occurred: {str(e)}")
        return None

with gr.Blocks(title="Empathy Engine", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🧠 The Empathy Engine
    """)

    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Enter your text",
                lines=3,
                placeholder="e.g., 'I'm so happy!' or 'This is frustrating.'",
                interactive=True
            )
            submit_btn = gr.Button("🎤 Speak with Emotion", variant="primary")

        with gr.Column(scale=1):
            audio_output = gr.Audio(
                label="Empathetic Speech Output",
                type="filepath",
                interactive=False
            )

    gr.Examples(
        examples=[
            "I am absolutely thrilled with this amazing news!",
            "I'm feeling really down today, nothing seems to go right.",
            "This is absolutely unacceptable! I demand an explanation.",
            "Wow! That was completely unexpected!",
            "The meeting is scheduled for tomorrow at 3 PM."
        ],
        inputs=text_input,
        label="Try these examples"
    )

    submit_btn.click(
        fn=generate_empathetic_speech,
        inputs=text_input,
        outputs=audio_output
    )

    text_input.submit(
        fn=generate_empathetic_speech,
        inputs=text_input,
        outputs=audio_output
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)