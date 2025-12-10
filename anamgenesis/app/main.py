import streamlit as st
from datetime import datetime

st.title("Anamgenesis")
st.write("You could start the app!")
btn = st.button("Click me")
if btn:
    st.write(f"Time: {datetime.now()}")
