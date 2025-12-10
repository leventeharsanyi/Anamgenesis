import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
secret_message = os.getenv("MY_SECRET_MESSAGE", "ERROR!!!!")

st.title("Anamgenesis")
st.write("You could start the app!")
btn = st.button("Click me")
if btn:
    st.write("Message from .env:")
    st.code(secret_message)
    st.write(f"Time: {datetime.now()}")
