import gradio as gr
import os
from debate_engine import run_debate_generator  # Updated import to avoid circular reference
from referee_bot import analyze_debate  # Import referee bot

def debate_stream():
    transcript = []
    with open("debate_transcript.txt", "w", encoding="utf-8") as file:
        for speaker, entry in run_debate_generator():
            transcript.append((speaker, entry))  # Store convo as tuple (Speaker, Message)
            file.write(f"{speaker}: {entry}\n")  # Save to transcript file
            file.flush()
            yield transcript, gr.update(interactive=False)  # Disable result button until debate ends
    yield transcript, gr.update(interactive=True)  # Enable result button when debate finishes

def referee_output():
    if not os.path.exists("debate_transcript.txt"):  # Check if transcript exists
        return "Error: Debate transcript not found! Run the debate first."
    
    analyze_debate()  # Call referee bot only if transcript exists
    with open("debate_result.txt", "r", encoding="utf-8") as result_file:
        return result_file.read()

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Debate: Steve Jobs vs Elon Musk")
    gr.Markdown("Watch an AI-powered debate unfold in real time and get an evaluation from our referee bot.")

    debate_btn = gr.Button("▶ Start Debate")
    result_btn = gr.Button("✅ Get Result", interactive=False)  # Initially disabled
    transcript_output = gr.Chatbot(label="Debate Chat", bubble_full_width=False, height=600)  # Bigger Chat UI
    result_output = gr.Textbox(label="Debate Verdict", interactive=False, lines=8)

    debate_btn.click(fn=debate_stream, outputs=[transcript_output, result_btn])  # Start debate
    result_btn.click(fn=referee_output, outputs=result_output)  # Get result

if __name__ == "__main__":
    demo.launch()
