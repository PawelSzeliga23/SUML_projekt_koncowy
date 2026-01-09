"""
Main application file for the Streamlit app.
"""

import streamlit as st
from views import navigation
from models import yolo_init


def main():
    """
    Main function to run the Streamlit app.
    :return:
    """
    st.set_page_config(layout="wide")

    yolo_init.load_model()

    navigation.navigation()


if __name__ == "__main__":
    main()
