import speech_recognition as sr
import webbrowser
import pyttsx3
# import time
import winsound  # for beep sounds on Windows
import musicLibrary
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
from client import client  # Importing the OpenAI client from client.py
from datetime import datetime
import random


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

def speak(text):
    print(f"[DEBUG] Speaking: {text}")
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    # time.sleep(0.2)
    print("[DEBUG] Finished speaking")

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
    now = datetime.now()

     # --- Local time and date ---
     # --- Handle any combination of day/month/year/time ---
    date_time_parts = []

    if "day" in command:
        date_time_parts.append(f"Today is {now.strftime('%A')}")
    if "month" in command:
        date_time_parts.append(f"This month is {now.strftime('%B')}")
    if "year" in command:
        date_time_parts.append(f"The year is {now.strftime('%Y')}")
    if "time" in command:
        date_time_parts.append(f"The time is {now.strftime('%I:%M %p')}")

    if date_time_parts:
        speak(" and ".join(date_time_parts))
        return

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return

    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        return

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
        return

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        return

 # --- Play music ---
    elif "play" in command:
        song = command.replace("play", "").strip() # get everything after play
        link = musicLibrary.music.get(song)
        
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
        return

##### news #####
    elif "news" in command:
        speak("Fetching the latest news headlines")
        
        try:
            response = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            )
            
            if response.status_code == 200:
                data = response.json()
                print("[DEBUG] Full API response:", data)  # See exactly what we got

                articles = data.get("articles", [])
                if articles:
                    for article in articles[:5]: # Limit to first 5 articles
                        title = article.get("title", "No title available")
                        speak(title)
                        print(f"[DEBUG] News: {title}")
                else:
                    speak("No news articles found at the moment.")
            else:
                speak(f"News API returned status code {response.status_code}")
                print(f"[DEBUG] API Error: {response.text}")

        except Exception as e:
            speak("Sorry, I couldn't fetch the news at this time.")
            print(f"[DEBUG] Error fetching news: {e}")
        return

    else:
        #now openAI will be used to process the command or handle the request
        output= aiProcess(command)
        if output:
            speak(output)
        else:
            speak("I didn't understand that command. Please try again.")
        return
    

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
