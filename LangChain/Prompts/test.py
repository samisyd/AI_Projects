from temperature import model
import streamlit as st

st.header('Chatbot Application')

usr_input = st.text_input("Enter your prompt:")

if st.button('Summareize'):
    result = model.invoke(usr_input)
    st.write(result.content)