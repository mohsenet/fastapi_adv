# File: app.py
import streamlit as st
import requests

st.title("FastAPI + Streamlit Integration")
st.write("Enter two numbers to add them using FastAPI backend.")

a = st.number_input("Enter number A:", value=0)
b = st.number_input("Enter number B:", value=0)

if st.button("Add"):
    try:
        response = requests.get(f"http://localhost:8000/add?a={a}&b={b}")
        if response.status_code == 200:
            result = response.json()["result"]
            st.success(f"Result from FastAPI: {result}")
        else:
            st.error("Error from API")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI backend. Is it running?")
