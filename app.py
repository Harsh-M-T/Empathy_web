import pyttsx3
from textblob import TextBlob

def detect_emotion(text: str) -> str:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def get_voice_params(emotion: str) -> dict:
    params = {"rate": 175, "pitch": 0.0}

    if emotion == "positive":
        params["rate"] = 200
        params["pitch"] = 0.2
    elif emotion == "negative":
        params["rate"] = 140
        params["pitch"] = -0.2
    elif emotion == "neutral":
        params["rate"] = 175
        params["pitch"] = 0.0
    return params

def speak_with_emotion(text: str, output_filename: str = "output.wav") -> str:
    emotion = detect_emotion(text)
    print(f"Detected Emotion: {emotion}")

    params = get_voice_params(emotion)
    print(f"Applying Parameters: Rate={params['rate']}")

    engine = pyttsx3.init()
    engine.setProperty('rate', params['rate'])

    engine.save_to_file(text, output_filename)
    engine.runAndWait()
    return output_filename

if __name__ == "__main__":
    print("Welcome to the Empathy Engine!")
    user_input = input("Enter the text you'd like to hear: ")

    audio_file = speak_with_emotion(user_input)

    print(f"Your empathetic audio has been saved to: {audio_file}")