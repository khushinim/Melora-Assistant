# commands/news_commands.py
import requests
import os
from utils import speak
from dotenv import load_dotenv

load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

def handle_news(command):
    if "news" in command:
        speak("Fetching the latest news headlines")
        try:
            response = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            )
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                if articles:
                    for article in articles[:5]:
                        title = article.get("title", "No title available")
                        speak(title)
                else:
                    speak("No news articles found at the moment.")
            else:
                speak(f"News API returned status code {response.status_code}")
        except Exception as e:
            speak("Sorry, I couldn't fetch the news at this time.")
        return True
    return False
