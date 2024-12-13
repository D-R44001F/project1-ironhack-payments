import streamlit as st
import base64

def app():
    st.markdown("### Data Analytic & Conclusions Presentation")

    # Open the file as binary
    try:
        with open("./images/presentation.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        
        # Change the PDF to base64 to inset in Web Page
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
      
        # st.write("Presentation Preview")
        # Create an IFrame
        pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="800" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        # Download button
        st.download_button(
            label="Download Presentation",
            data=pdf_bytes,  # Send the binary code
            file_name="presentation.pdf",
            mime="application/pdf"  # Set MIME TYPE file
        )
    except FileNotFoundError:
        st.error("PDF File Not Found.")
    except Exception as e:
        st.error(f"Error: {e}")
       

    