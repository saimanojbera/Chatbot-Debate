# AI Debate System

## **Introduction**
This project is an **AI-powered debate system** where **Steve Jobs and Elon Musk** engage in a structured, dynamic conversation. The debate is displayed in a **real-time chat interface** with a referee bot analyzing the discussion and determining the winner.

## **Features**
- 📢 **Live Debate Streaming** – Watch an AI-generated discussion in a **WhatsApp-style chat UI**.
- 🤖 **AI Debaters** – Steve Jobs uses **GPT-4o**, and Elon Musk uses **LLaMA-3.3 via Groq API**.
- 🎯 **Referee Bot** – Analyzes the transcript and determines the winner based on **logic, innovation, and impact**.
- 🚀 **Dynamic UI** – Enlarged chat interface (`height=600`) for improved readability.
- ⏳ **Controlled Evaluation** – "✅ Get Result" button remains disabled until the debate ends.

---

## **Project Structure**
```
📂 AI-Debate-System/
│── debate_engine.py        # Handles debate logic and response sequencing
│── debate_interface.py     # Gradio UI for chat-style real-time debate
│── steve_jobs_bot.py       # AI model generating Steve Jobs' responses
│── elon_musk_bot.py        # AI model generating Elon Musk's responses
│── referee_bot.py          # AI referee evaluating the debate
│── .env                    # Stores API keys for OpenAI and Groq API
│── debate_transcript.txt   # Stores full debate conversation log
│── debate_result.txt       # Stores the final referee verdict
│── README.md               # Project documentation (this file)
```

---

## **Installation & Setup**
### **1️⃣ Install Dependencies**
Ensure you have Python installed. Then, install the required libraries:
```sh
pip install openai groq gradio python-dotenv
```

### **2️⃣ Set Up API Keys**
Create a `.env` file in the project directory and add your **OpenAI and Groq API keys**:
```
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### **3️⃣ Run the Debate System**
Start the Gradio interface:
```sh
python debate_interface.py
```

---

## **Usage Guide**
1️⃣ **Click "▶ Start Debate"** – Steve Jobs and Elon Musk begin debating in real-time.  
2️⃣ **Watch the Debate** – Their responses appear in a structured, chat-style UI.  
3️⃣ **Wait Until the Debate Ends** – The "✅ Get Result" button remains disabled.  
4️⃣ **Click "✅ Get Result"** – The Referee Bot evaluates the debate and announces the winner.

---

## **Customization**
- 🎨 **UI Enhancements** – Modify `debate_interface.py` to adjust chat bubble size, colors, etc.
- 🏆 **Additional AI Debaters** – Extend `debate_engine.py` to add new AI characters.
- 🔊 **Voice Support** – Integrate **text-to-speech (TTS)** for audio-based debates.

---

## **Credits & References**
- OpenAI API for Steve Jobs Bot  
- Groq API for Elon Musk Bot  
- Gradio for real-time UI interaction  

🚀 **Enjoy the AI Debate System!** 🎤🔥

