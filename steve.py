import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_steve_response(prompt, conversation_history=[]):
    messages = [
        {"role": "system", "content": "You are Steve Jobs, co-founder of Apple, focusing on innovation, design, and user experience."}
    ]

    conversation_history = conversation_history[-6:]  # Keep last 6 exchanges

    for conv in conversation_history:
        messages.append({"role": "assistant", "content": conv})

    messages.append({"role": "user", "content": prompt})

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.8
    )

    return response.choices[0].message.content
