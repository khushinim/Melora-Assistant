from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()  # load .env

openaiapi = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openaiapi)

