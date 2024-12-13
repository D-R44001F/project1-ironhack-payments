import streamlit as st
from multiapp import MultiApp
import home
import about
import data
import explore
import clean
import analyze
import presentation

# Dashboard Configuration
st.set_page_config(
    page_title="IronHack Bootcamp - Project 1 Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
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
# app.add_app("Demo", data.app)

# Run the Webapp
app.run()
