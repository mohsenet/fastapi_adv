"""
# How to run this code:
# Save it and run the following command in terminal

streamlit run
"""


import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")

# Display a header
st.header("Welcome!")

# Display text
st.write("This is a simple example of a Streamlit app.")

# Add an input widget (text input)
name = st.text_input("Enter your name:")

# Add a button and display output conditionally
if st.button("Say Hello"):
    st.write(f"Hello, {name}! 👋")
else:
    st.write("Please enter your name and click the button.")
