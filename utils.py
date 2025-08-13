# utils.py
import pyttsx3

def speak(text):
    print(f"[DEBUG] Speaking: {text}")
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    print("[DEBUG] Finished speaking")
