import speech_recognition as sr
import webbrowser
import pyttsx3
# import time
import winsound  # for beep sounds on Windows
import musicLibrary

recognizer = sr.Recognizer()
#engine = pyttsx3.init(driverName='sapi5')


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

def processCommand(c):
    if c.lower() == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif c.lower() == "open youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif c.lower() == "open facebook":
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif c.lower() == "open twitter":
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif c.lower() == "open instagram":
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif c.lower() == "open whatsapp":
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    elif c.lower() == "open linkedin":
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower() == "open github":
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()  # get everything after "play"
        link = musicLibrary.music.get(song)
        
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    

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
