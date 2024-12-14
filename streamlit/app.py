import streamlit as st
from multiapp import MultiApp
import home
import about
import data
import explore
import clean
import analyze
import presentation
import dashboard

# Dashboard Configuration
st.set_page_config(
    page_title="IronHack Bootcamp - Project 1 Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .main {
            padding-top: 2px; /* Reduce el padding superior */
        }
        .main > div {
            padding-top: 2px; /* Reduce el padding superior */
        }
        h1 {
            margin-top: -20px; /* Ajusta el margen superior del título */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dashboard Title
st.title("IronHack Bootcamp - Project 1 Dashboard")

# Create the MultiApp Instance for multiple pages
app = MultiApp()

# Register the webpages
app.add_app("Home", home.app)
app.add_app("About", about.app)
app.add_app("Explore Process", explore.app)
app.add_app("Clean Process", clean.app)
app.add_app("Vizualize & Analyze Process", analyze.app)
app.add_app("Presentation", presentation.app)
app.add_app("Dashboard", dashboard.app)
# app.add_app("Demo", data.app)

# Run the Webapp
app.run()
