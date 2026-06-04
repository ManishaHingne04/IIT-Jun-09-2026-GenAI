import streamlit as st

with st.form(key="login_form"):
    st.header("User Login")
    user = st.text_input("Enter Username...")
    passwd = st.text_input("Enter Passwd...", type="password")
    signin = st.form_submit_button("Sign In")

if signin:
    if user == passwd:
        st.success("Login Successful!!")
    else:
        st.error("Login Failed!!!")