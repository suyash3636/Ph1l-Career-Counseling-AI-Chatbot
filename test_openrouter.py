import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"  # ✅ required for OpenRouter
)

response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    messages=[
        {"role": "system", "content": "You are a career counselor for Indian students."},
        {"role": "user", "content": "I'm studying electronics but want to switch to AI."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
