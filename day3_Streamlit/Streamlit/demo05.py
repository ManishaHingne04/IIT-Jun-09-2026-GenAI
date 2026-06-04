import streamlit as st

case = "Upper"

with st.sidebar:
    st.header("Settings")
    case = st.selectbox("Select: ", ["Upper", "Lower", "Toggle"])
    maxcnt = st.slider("Max Messages: ", max_value=10)
    st.subheader("Current Config")
    st.json({
        "Case: ": case,
        "Max: ": maxcnt
    })
    st.button("Clear History")


# initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# update the session state
message = st.chat_input("Say something...")
if message:
    st.session_state.messages.append("user:" + message)
    if case == "Upper":
        result = message.upper()
    elif case == "Lower":
        result = message.lower()
    else: # toggle case
        result = message.swapcase()
    st.session_state.messages.append("ai:" + result)

# display the session state
for msg in st.session_state.messages:
    if msg.startswith("user:"):
        role = "user"
    else:
        role = "ai"
    with st.chat_message(role):
        st.write(msg)

# Assignment: Display only limited number of messages in chat history (as set in slider).
