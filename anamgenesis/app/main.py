import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

from anamgenesis.app.model_calls import generate_voice, generate_text

load_dotenv()
secret_message = os.getenv("MY_SECRET_MESSAGE", "ERROR!!!!")


st.title("Anamgenesis")
st.subheader("Test the system.")
st.write("You could start the app!")
if st.button("Check the health status of the system."):
    st.write("Message from .env:")
    st.code(secret_message)
    st.write(f"Time: {datetime.now()}")

st.subheader("TTS model.")
with st.expander("Open the TTS part."):
    text_to_speak = st.text_area(
        label="Text to speak",
        placeholder="Type here...",
        height=100
    )
    if st.button("Generate audio"):
        generate_voice(text=text_to_speak)

st.subheader("STT model.")
with st.expander("Open the STT part."):
    audio_file = st.audio_input("Record your voice here:", sample_rate=48000)
    if audio_file is not None:
        st.write("Your voice was recorded successfully!")
        if st.button("Send to agent and speak back."):
            transcription_text = generate_text(audio_input=audio_file)
            st.write("Response from agent:")
            generate_voice(text="This is what you said: " + transcription_text + "Nice Job Mate!")
