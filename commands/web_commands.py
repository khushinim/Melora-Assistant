import webbrowser
from utils import speak


def handle_web(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return True
    elif "twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        return True
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return True
    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
        return True
    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return True
    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        return True
    return False