🤖🗣️ Speech + Text Chatbot App

This is a hybrid chatbot application built with **Streamlit** that accepts **both voice and text input**, processes it, and returns a chatbot-like response. The app combines **Google Speech Recognition API** and a simple rule-based chatbot backend.

🎯 Features

- 🎤 **Voice Recognition** using Google Speech-to-Text
- 💬 **Text Chat** mode
- 🤖 Rule-based responses using a dictionary
- 🧠 Easily extensible to use NLP, NLTK, or deep learning models
- ⚡ Real-time interaction in a web interface

🛠 Technologies Used

- Python 🐍
- Streamlit
- SpeechRecognition (Google API)
- NLTK (for future NLP integration)
- Microphone input via PyAudio (local only)

⚙️ Installation

bash
git clone https://github.com/your-username/speech-text-chatbot.git
cd speech-text-chatbot
pip install -r requirements.txt
📝 Requirements
Your requirements.txt should include:

nginx
Copy
Edit
streamlit
speechrecognition
pyaudio
nltk
🔧 Note: pyaudio may require system dependencies (e.g., portaudio on macOS/Linux).

🚀 Running the App
bash
Copy
Edit
streamlit run app.py
📌 This app must be run locally to access your device's microphone for voice input.

🧠 How It Works
If the user selects Text Input, they can chat with the bot via typing.

If the user selects Speech Input, they click "Start Recording", speak into the mic, and the app transcribes the speech to text.

The user input is matched against a simple dictionary of responses:

python
Copy
Edit
chatbot_data = {
    "hello": "Hi there! How can I help you?",
    "bye": "Goodbye! Have a great day!"
}
Future expansion can connect this to an NLP or ML chatbot model using transformers, spaCy, or Rasa.

📁 Example Interaction
makefile
Copy
Edit
You: hello
Chatbot: Hi there! How can I help you?
👤 Author
Ziggy Greg
GitHub • Instagram

📜 License
MIT License — free to use, share, and modify.
