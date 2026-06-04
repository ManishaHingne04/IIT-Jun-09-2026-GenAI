import streamlit as st

st.write("Hello Text")

text = """
Streamlit is an open-source Python framework for data scientists 
and AI/ML engineers to deliver dynamic data apps with only a few lines of code. 
Build and deploy powerful data apps in minutes. Let's get started!

rocket_launch
Get started with Streamlit! Set up your development environment and learn the fundamental concepts, and start coding!

description
Develop your Streamlit app! Our API reference explains each Streamlit function with examples. Dive deep into all of our features with conceptual guides. Try out our step-by-step tutorials.

cloud
Deploy your Streamlit app! Streamlit Community Cloud our free platform for deploying and sharing Streamlit apps. Streamlit in Snowflake is an enterprise-class solution where you can house your data and apps in one, unified, global system. Explore all your options!

school
Knowledge base is a self-serve library of tips, tricks, and articles that answer your questions about creating and deploying Streamlit apps.
"""

gen = (ch for ch in text)
st.write_stream(gen)