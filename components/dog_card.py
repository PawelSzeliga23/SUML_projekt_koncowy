import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def dog_card(breed_name: str, image_path: str, confidence: float):
    """
    Display a card with dog breed information.

    Parameters:
    breed_name (str): The name of the dog breed.
    image_path (str): The path to the image of the dog breed.
    description (str): A brief description of the dog breed.
    """
    response = requests.get(image_path)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    col1, col2 = st.columns([4, 7])
    with col1:
        st.image(image)
    with col2:
        st.subheader(breed_name)
        st.metric(label="Pewność wykrycia", value=f"{confidence * 100:.1f}%")
    progress_bar = st.progress(0)
    progress_bar.progress(int(confidence * 100))

