import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def analyze_debate():
    with open("debate_transcript.txt", "r", encoding="utf-8") as file:
        debate_text = file.read()

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an unbiased AI referee, evaluating a debate based on logical reasoning, impact, innovation, and argument strength."},
            {"role": "user", "content": f"Evaluate this debate and declare a winner:\n\n{debate_text}"}
        ],
        temperature=0.7
    )

    verdict = response.choices[0].message.content

    with open("debate_result.txt", "w", encoding="utf-8") as result_file:
        result_file.write(verdict)

    return verdict
