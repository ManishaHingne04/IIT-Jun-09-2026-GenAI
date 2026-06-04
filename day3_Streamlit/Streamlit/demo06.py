import streamlit as st

def show_home_page():
    st.title("Home")
    # ...

def show_aboutus_page():
    st.title("About Us")
    # ...

def show_contactus_page():
    st.title("Contact Us")
    # ...

def show_courses_page():
    st.title("Courses")
    # ...

def show_branches_page():
    st.title("Branches")
    # ...

page = "Home"

with st.sidebar:
    if st.button("Home"):
        page = "Home"
    if st.button("About Us"):
        page = "About Us"
    if st.button("Contact Us"):
        page = "Contact Us"
    if st.button("Courses"):
        page = "Courses"
    if st.button("Branches"):
        page = "Branches"

if page == "Home":
    show_home_page()
elif page == "About Us":
    show_aboutus_page()
elif page == "Contact Us":
    show_contactus_page()
elif page == "Courses":
    show_courses_page()
elif page == "Branches":
    show_branches_page()
