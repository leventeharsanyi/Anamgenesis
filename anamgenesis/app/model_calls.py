import io
import os

import streamlit as st
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key is None:
    raise ValueError("Missing ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)


def generate_voice(text: str) -> None:
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )
    audio_bytes = b"".join(audio)
    st.success("Audio generated successfully!")
    st.audio(audio_bytes)


def generate_text(audio_input):
    audio_data = io.BytesIO(audio_input.getvalue())
    transcription = client.speech_to_text.convert(
        file=audio_data,
        model_id="scribe_v1",
        tag_audio_events=False,
        language_code="eng",
        diarize=False,
    )
    text = transcription.text
    st.write("This is what you said:")
    st.write(text)
    return text
