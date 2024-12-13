import streamlit as st

def app():
    st.title("Data")
    st.write("Demo Page with Graph.")
    st.line_chart([1, 2, 3, 4, 5])
