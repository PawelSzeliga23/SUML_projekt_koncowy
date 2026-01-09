"""
Component to display a dog breed card with image, breed name, and confidence level.
"""
import streamlit as st


def dog_card(breed_name: str, image, confidence: float):
    """
    Display a dog breed card with image, breed name, and confidence level.
    :param breed_name:
    :param image:
    :param confidence:
    :return: streamlit component
    """
    col1, col2 = st.columns([4, 7])

    with col1:
        st.image(image)
    with col2:
        st.subheader(breed_name)
        if confidence is not None:
            st.metric(label="Pewność wykrycia", value=f"{confidence * 100:.1f}%")

    if confidence is not None:
        progress_bar = st.progress(0)
        progress_bar.progress(int(confidence * 100))
