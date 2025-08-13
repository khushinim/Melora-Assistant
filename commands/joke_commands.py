# commands/joke_commands.py
from utils import speak
import random

JOKES = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why was the cell phone wearing glasses? It lost its contacts!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why do Java developers wear glasses? Because they don’t see sharp!"
]

def handle_joke(command):
    """
    Check if the user asked for a joke.
    Returns True if handled.
    """
    if "joke" in command:
        speak(random.choice(JOKES))
        return True
    return False
