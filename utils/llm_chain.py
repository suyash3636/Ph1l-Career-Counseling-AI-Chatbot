from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from utils.prompts import career_counselor_prompt
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env if not already done

def create_chain():
    api_key = os.getenv("OPENROUTER_API_KEY")

    # Debug print to confirm
    print("✅ OpenRouter API key loaded:", api_key[:10] if api_key else "❌ NOT FOUND")

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",  # or mistral-small
        temperature=0.5,
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=api_key,  # ✅ Must be passed like this
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=career_counselor_prompt,
        verbose=False
    )

    return chain
