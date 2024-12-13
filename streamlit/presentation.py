import streamlit as st

def app():

    st.title("Visualizations")

    with open("./images/presentation.pdf") as pdf_file:
        st.download_button(label="Download", data=pdf_file, file_name="presntation.pdf")
        st.write("Presentation Preview")
        st.pdf(pdf_file)