import streamlit as st

# init count in session state
if 'count' not in st.session_state:
    st.session_state.count=0

st.title("My Counter App")

col1, col2 = st.columns(2)
with col1:
    if st.button("Increment"):
        st.session_state.count = st.session_state.count + 1
with col2:
    if st.button("Reset"):
        st.session_state.count = 0

st.markdown(f"### Count = {st.session_state.count}")
