from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import streamlit as st
import io

from PIL import Image

#loading environment variable
load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")


#initializing a client
client = genai.Client(api_key=my_api_key)


#Note Generator
def note_generator(images):
    
    prompt = """Summarize the pictures in note format at max 100 words
    make sure to add necessary markdown to diffentiate different section"""
    
    response = client.models.generate_content(model="gemini-3-flash-preview",
                                   contents=[images, prompt])
    
    return response.text


#Audio Transcription
def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer


#Quiz Generator
def quiz_generator(images, difficulty):
    
    prompt = f"""Generate 3 quizzes based on the {difficulty}.Make sure to add the markdown to differentiate the options.Add correct answers too after the quiz"""
    
    response = client.models.generate_content(model="gemini-3-flash-preview",
                                   contents=[images, prompt])
    
    return response.text
