import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload the photos of your note",
                     type=["jpg", "jpeg", "png"],
                     accept_multiple_files=True)
    
    pill_images = []
    for img in images:
        pill_img = Image.open(img)
        pill_images.append(pill_img)
    
    #images
    if images:
        if len(images) > 3:
            st.error("Uplod at max three images")
        
        else:
            col = st.columns(len(images))

            st.subheader("Uploaded images")
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty
    selected_option = st.selectbox("Enter the difficulty of Quiz",
                 ("Easy", "Medium", "Hard"),
                 index=None)
    
    pressed = st.button("Click the button to initiate AI", type="primary")
    
if pressed:
    if not images:
        st.error("You must upload at least 1 image")
        
    if not selected_option:
        st.error("You must select a difficulty")
        
    if images and selected_option:
        
        #Note
        with st.container(border=True):
            st.subheader("Your note")
            
            with st.spinner("AI is generating notes for you..."):
                generated_notes = note_generator(pill_images)
                st.markdown(generated_notes)
        
        #Audio transcription
        with st.container(border=True):
            st.subheader("Audio Transcription")
            
            generated_notes = generated_notes.replace("#", "")
            generated_notes = generated_notes.replace("-", "")
            generated_notes = generated_notes.replace("*", "")
            generated_notes = generated_notes.replace("`", "")
            
            with st.spinner("AI is generating transcripting for you..."):
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)
            
        #Quiz
        with st.container(border=True):
            
            st.subheader(f"Quiz: {selected_option} Difficulty") 
            
            with st.spinner("AI is generating Quizzes for you..."):
                quizzes = quiz_generator(pill_images, selected_option)
                st.markdown(quizzes)