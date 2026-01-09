"""
Module to load YOLO model for dog breed classification.
"""

from ultralytics import YOLO
import streamlit as st


@st.cache_resource
def load_model(model_path="models/pretrained/yolo11_dog_breed.pt"):
    """
    Load the YOLO model from the specified path.
    :param model_path:
    :return: YOLO model instance
    """
    return YOLO(model_path)


MODEL = load_model("models/pretrained/best.pt")
