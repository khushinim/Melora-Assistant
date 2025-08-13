# commands/music_commands.py
import webbrowser
from utils import speak
import musicLibrary

def handle_music(command):
    if "play" in command:
        song = command.replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
        return True
    return False
