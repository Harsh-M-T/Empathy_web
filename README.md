# The Empathy Engine 

The Empathy Engine dynamically modulates the vocal characteristics of synthesized speech based on the detected emotion of the input text. It leverages a **Small Language Model (SLM)** for nuanced emotion detection and **Microsoft Edge TTS** with **SSML** to produce expressive, natural‑sounding audio.

---

## Features

- **Advanced Emotion Detection**  
  Uses [`the-robot-ai/tiny-emotion`](https://huggingface.co/the-robot-ai/tiny-emotion), a lightweight SLM fine‑tuned for emotion classification. Detects `joy`, `sadness`, `anger`, `surprise`, `fear`, and `neutral`.

- **Dynamic Voice Modulation via SSML**  
  Emotion → SSML mapping alters:
  - **Rate** (speaking speed)
  - **Pitch** (tonal height)

- **Web Interface (Gradio)**  
  Interactive UI for instant text‑to‑empathetic‑speech conversion.

- **Command‑Line Interface**  
  Run the engine directly from the terminal.

- **Fully Offline & Free**  
  No API keys required. The SLM and TTS run locally or via free public endpoints.

### Prerequisites

- **Python 3.9 – 3.11** (3.12 works but may have minor dependency issues)
- `pip` (Python package manager)


### USAGE

```bash
    git clone https://github.com/yourusername/empathy-engine.git
    cd empathy-engine
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python web_app.py
```

### Visibility
- Open your browser at http://127.0.0.1:7860.