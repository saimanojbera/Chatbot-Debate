from steve import generate_steve_response
from elon import generate_elon_response

def run_debate_generator():
    conversation_history = []
    user_prompt = "Who has contributed more to the greater advancement of technology in society?"

    with open("debate_transcript.txt", "w", encoding="utf-8") as file:
        for round_num in range(50):  # Debate will run for 50 turns
            if round_num % 2 == 0:
                speaker = "Steve Jobs"
                response = generate_steve_response(user_prompt, conversation_history)
            else:
                speaker = "Elon Musk"
                response = generate_elon_response(user_prompt, conversation_history)

            entry = f"{speaker}: {response}"
            conversation_history.append(entry)

            file.write(entry + "\n")
            file.flush()

            user_prompt = f"{response} What do you think about this, {('Elon Musk' if speaker == 'Steve Jobs' else 'Steve Jobs')}?"

            yield speaker, response  # Yield for Gradio UI
