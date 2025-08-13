import speech_recognition as sr
from utils import speak

# import time
import winsound  # for beep sounds on Windows
import os
from dotenv import load_dotenv
from openai import OpenAI
from client import client  # Importing the OpenAI client from client.py
from commands import web_commands, music_commands, news_commands, datetime_commands, joke_commands



recognizer = sr.Recognizer()
#engine = pyttsx3.init(driverName='sapi5')
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")
openaiapi = os.getenv("OPENAI_API_KEY")


# === Beep Sounds ===
def play_beep_start():
    winsound.Beep(1000, 200)  # High-pitch start beep

def play_beep_end():
    winsound.Beep(700, 200)   # Lower-pitch end beep

# Uses OpenAI to respond to a command that is not recognized by other predefined actions.
def aiProcess(command):
    speak("Let me think about that...")
    try:
        response = client.responses.create(
            model="gpt-5",
            input=f"User said: '{command}'. Respond helpfully."
        )
        reply = response.output_text
        speak(reply)
        print(f"[DEBUG] AI Response: {reply}")
        return reply
    except Exception as e:
        speak("Sorry, I couldn't process that request.")
        print(f"[DEBUG] OpenAI Error: {e}")
        return None


def processCommand(c):
    command = c.lower()
    
     # Local commands
    if datetime_commands.handle_datetime(command):
        return
    if joke_commands.handle_joke(command):
        return
    if web_commands.handle_web(command):
        return
    if music_commands.handle_music(command):
        return
    if news_commands.handle_news(command):
        return

    # AI fallback
    aiProcess(command)

if __name__ == "__main__":
    speak("Initializing Melora...")

    while True:
        # Recognizing the audio input
        try:
             # Will listen for activation word or wake word "Melora", audio obtained from the microphone
            with sr.Microphone() as source:
                print("Listening for wake word...")
                # recognizer.adjust_for_ambient_noise(source, duration=0.5)
                play_beep_start()
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                play_beep_end()

            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")

            if word.lower() == "melora":
                speak("Yaa")
                print("Melora Activated...")

               
                # time.sleep(0.3)

                
                # listen for commands after activation
                with sr.Microphone() as source:
                    print("Listening for command...")
                    # recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    play_beep_start()
                    audio = recognizer.listen(source)
                    play_beep_end()
                    
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)


            # if "exit" in command.lower():
            #     speak("Goodbye!")
            #     break

        # except Exception as e:
        #         print("Error; {}".format(e))
        except sr.WaitTimeoutError:
            print("No speech detected. Listening again...")
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except sr.RequestError:
            print("Network error with speech recognition service.")
