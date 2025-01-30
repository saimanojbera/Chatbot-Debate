import groq
import os
import time
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_elon_response(prompt, conversation_history=[]):
    messages = [
        {"role": "system", "content": "You are Elon Musk, an entrepreneur revolutionizing space, AI, and electric vehicles. You focus on first-principles thinking."}
    ]

    # Save user input to debate transcript
    with open("debate_transcript.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {prompt}\n")

    # Keep only the last 6 exchanges (to maintain token limits)
    recent_history = conversation_history[-6:]

    for i in range(0, len(recent_history), 2):
        if i + 1 < len(recent_history):
            messages.append({"role": "user", "content": recent_history[i]})
            messages.append({"role": "assistant", "content": recent_history[i + 1]})

    messages.append({"role": "user", "content": prompt})

    client = groq.Client(api_key=GROQ_API_KEY)

    # Retry mechanism for rate limit handling
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.8
            )

            elon_response = response.choices[0].message.content

            # Save response to transcript
            with open("debate_transcript.txt", "a", encoding="utf-8") as file:
                file.write(f"Elon Musk: {elon_response}\n")

            return elon_response

        except groq.RateLimitError as e:
            error_message = e.response.json().get("error", {}).get("message", "")
            if "Please try again in" in error_message:
                wait_time = int(error_message.split(" in ")[-1].split("s")[0])
                print(f"Rate limit reached. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Rate limit exceeded. Retrying in 60 seconds...")
                time.sleep(60)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "Error: Unable to generate response at this time."

    return "Error: Reached maximum retry attempts. Please try again later."
