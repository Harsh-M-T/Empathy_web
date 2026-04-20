import asyncio
import edge_tts
from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="the-robot-ai/tiny-emotion", top_k=1)
print("Emotion classifier loaded.")

def get_voice_params(emotion_label: str) -> dict:
    params = {"rate": "+0%", "pitch": "+0Hz"}
    if emotion_label == "joy":
        params["rate"] = "+20%"
        params["pitch"] = "+15Hz"
    elif emotion_label == "sadness":
        params["rate"] = "-15%"
        params["pitch"] = "-10Hz"
    elif emotion_label == "anger":
        params["rate"] = "+30%"
        params["pitch"] = "+20Hz"
    elif emotion_label == "surprise":
        params["rate"] = "+10%"
        params["pitch"] = "+25Hz"
    elif emotion_label == "fear":
        params["rate"] = "+15%"
        params["pitch"] = "+5Hz"
    return params

async def speak_with_emotion(text: str, output_filename: str = "output.mp3") -> str:
    results = emotion_classifier(text)
    detected_emotion = results[0][0]['label'] if results else "neutral"
    print(f"Detected Emotion: {detected_emotion}")

    voice_params = get_voice_params(detected_emotion)

    await edge_tts.Communicate(text, voice="en-US-AriaNeural", 
                               rate=voice_params['rate'], 
                               pitch=voice_params['pitch']).save(output_filename)
    
    print(f"Audio saved to: {output_filename}")
    return output_filename

def speak_with_emotion_sync(text: str, output_filename: str = "output.mp3") -> str:
    return asyncio.run(speak_with_emotion(text, output_filename))

if __name__ == "__main__":
    print("=" * 50)
    print(" Welcome to the Advanced Empathy Engine ")
    print("=" * 50)
    user_text = input("Enter text to speak: ")
    if user_text.strip():
        speak_with_emotion_sync(user_text)
        print("Done!")
    else:
        print("No text provided. Exiting.")