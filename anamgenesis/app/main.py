import os
import io
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()
secret_message = os.getenv("MY_SECRET_MESSAGE", "ERROR!!!!")
api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key is None:
    raise ValueError("Missing ELEVENLABS_API_KEY")


st.title("Anamgenesis")
st.subheader("Test the system.")
st.write("You could start the app!")
if st.button("Check the health status of the system."):
    st.write("Message from .env:")
    st.code(secret_message)
    st.write(f"Time: {datetime.now()}")

client = ElevenLabs(api_key=api_key)

st.subheader("TTS model.")


def generate_voice(text: str) -> None:
    global audio, audio_bytes
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )
    audio_bytes = b"".join(audio)
    st.success("Audio generated successfully!")
    st.audio(audio_bytes)


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
            audio_data = io.BytesIO(audio_file.getvalue())
            transcription = client.speech_to_text.convert(
                file=audio_data,
                model_id="scribe_v1",
                tag_audio_events=False,
                language_code="eng",
                diarize=False,
            )
            transcription_text = transcription.text
            st.write("This is what you said:")
            st.write(transcription_text)
            st.write("Response from agent:")
            generate_voice(text="This is what you said: "+transcription_text + "Nice Job Mate!")
