import streamlit as st


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Selection Bar
        st.sidebar.title("Navigation")
        app = st.sidebar.radio(
            "Select a Web Page:",
            self.apps,
            format_func=lambda app: app["title"]
        )
        # Run the associate function on the selecte web page
        app["function"]()
