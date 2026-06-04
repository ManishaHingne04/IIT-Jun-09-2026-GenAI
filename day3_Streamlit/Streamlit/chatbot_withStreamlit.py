import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Groq model
model = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=500
)

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot")

st.title("Groq Chatbot")

# User input
question = st.text_input("Ask a question:")

if st.button("Submit") and question:

    response_placeholder = st.empty()
    full_response = ""

    # Stream response
    for chunk in model.stream(question):
        full_response += chunk.content
        response_placeholder.markdown(full_response)

    st.success("Response completed!")