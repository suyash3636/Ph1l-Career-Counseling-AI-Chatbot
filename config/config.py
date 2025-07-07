import os
from dotenv import load_dotenv

load_dotenv()

def get_openrouter_key():
    return os.getenv("OPENROUTER_API_KEY")
