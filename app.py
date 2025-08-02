import streamlit as st

st.title("💻 Hello World from Streamlit!")
st.write("This is your first Python web app, deployed with 0 stress 😎")

user = st.text_input("Enter your name:")
if user:
    st.success(f"Welcome, {user}!")
