import streamlit as st
import speech_recognition as sr
import nltk
import os

# Load and preprocess chatbot data
def load_chatbot_data():
    # Placeholder for actual chatbot data processing
    return {"hello": "Hi there! How can I help you?", "bye": "Goodbye! Have a great day!"}

chatbot_data = load_chatbot_data()

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        try:
            audio_text = r.listen(source, timeout=5)
            st.info("Transcribing...")
            text = r.recognize_google(audio_text, language="en-US")
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the speech."
        except sr.RequestError:
            return "Could not request results, check your internet connection."
        except Exception as e:
            return f"An error occurred: {str(e)}"

def chatbot_response(user_input):
    return chatbot_data.get(user_input.lower(), "I'm not sure how to respond to that.")

def main():
    st.title("Speech & Text Chatbot")
    
    input_type = st.radio("Choose input method:", ("Text", "Speech"))
    user_input = ""
    
    if input_type == "Text":
        user_input = st.text_input("Enter your message:")
    elif input_type == "Speech":
        if st.button("Start Recording"):
            user_input = transcribe_speech()
            st.write("You said:", user_input)
    
    if user_input:
        response = chatbot_response(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
