import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text(lang="fa-IR"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=lang)
        print(f"You said: {text}")
        return text
    except Exception as e:
        print(f"Error: {e}")
        return "خطا در تشخیص گفتار"

def text_to_speech(text, lang="fa"):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    os.system("start response.mp3")
