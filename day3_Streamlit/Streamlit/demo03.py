import streamlit as st

# initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# update the session state
message = st.chat_input("Say something...")
if message:
    st.session_state.messages.append("user:" + message)
    st.session_state.messages.append("ai:" + message.upper())

# display the session state
for msg in st.session_state.messages:
    if msg.startswith("user:"):
        role = "user"
    else:
        role = "ai"
    with st.chat_message(role):
        st.write(msg)
