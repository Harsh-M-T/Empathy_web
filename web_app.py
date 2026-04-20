import gradio as gr
import soundfile as sf
import numpy as np
from app import speak_with_emotion, detect_emotion, get_voice_params

def generate_empathetic_speech(text):
    audio_file = speak_with_emotion(text, "gradio_output.wav")
    audio_data, sample_rate = sf.read(audio_file)
    return (sample_rate, audio_data)

demo = gr.Interface(
    fn=generate_empathetic_speech,
    inputs=gr.Textbox(label="Enter Text", lines=3, placeholder="Type something here..."),
    outputs=gr.Audio(label="Empathetic Speech Output"),
    title="The Empathy Engine",
    description="Transform text into emotionally resonant speech. The engine detects the sentiment and modulates pitch and speed to sound happy, frustrated, or neutral.",
)

if __name__ == "__main__":
    demo.launch()