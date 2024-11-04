import streamlit as st


st.title("Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Enter your age:", 0, 100, 25)

st.write(f"Hello {name}! You are {age} years old.")

option = ["python", "R", "Julia"]   

choice = st.selectbox("Choose your favorite language", option)

st.write(f"Your favorite language is {choice}.")

if name:
    st.write(f"Hello {name}!")



upload = st.file_uploader("Choose a file",type="pdf")

if upload is not None:
    st.write(upload.name)
    st.write(upload.size)
    st.write(upload.type)
    st.write(upload.getvalue()) 