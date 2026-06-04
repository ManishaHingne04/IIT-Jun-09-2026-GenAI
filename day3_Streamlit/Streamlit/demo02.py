import streamlit as st
import pandas as pd

# python text input on console
# name = input("Enter your name: ")
name = st.text_input("Enter your name: ")
message = st.text_area("Enter your message: ", height=100)
model = st.selectbox("Choose AI Model: ", ["GPT-5", "Gemini", "Claude"])

uplodaded_file = st.file_uploader("Choose a file: ")
if uplodaded_file:
    data = pd.read_csv(uplodaded_file)
    st.dataframe(data)
