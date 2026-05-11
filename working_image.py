import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")


#initializing a client
client = genai.Client(api_key=my_api_key)

images = st.file_uploader("Upload the photos of your note",
                          type=["jpg", "jpeg", "png"],
                          accept_multiple_files=True)


if images:
    pill_images = []
    for img in images:
        pill_img = Image.open(img)
        pill_images.append(pill_img)
    
    prompt = """Summarize the pictures in note format at max 100 words
    make sure to add necessary markdown to diffentiate different section"""
    
    response = client.models.generate_content(model="gemini-3-flash-preview",
                                   contents=[pill_images, prompt])
    
    st.markdown(response.text)
    