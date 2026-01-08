from ultralytics import YOLO
import streamlit as st


@st.cache_resource
def load_model(model_path="models/yolo11_dog_breed.pt"):
    """
    Load the YOLO model from the specified path.
    :param model_path:
    :return: YOLO model instance
    """
    return YOLO(model_path)


MODEL = load_model("models/best.pt")
