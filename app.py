import streamlit as st
import pyttsx3
from transformers import pipeline

# Initialize sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Adjust speaking speed

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Function to convert text to speech
def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Streamlit App UI
st.title("🎙️ Real-time Sentiment Analysis 🔊")

# Input text box
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input:
        label, confidence = analyze_sentiment(user_input)
        st.write(f"**Sentiment:** {label} (Confidence: {confidence:.2f})")

        # Speak sentiment result
        speak_text(f"The sentiment is {label} with confidence {confidence:.2f}")

    else:
        st.warning("Please enter some text before analyzing.")

# Enable voice output toggle
if st.checkbox("Enable Voice Output"):
    if user_input:
        speak_text(user_input)

# Footer
st.markdown("Developed by **Your Name** 💡")

