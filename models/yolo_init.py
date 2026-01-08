from ultralytics import YOLO
import streamlit as st


@st.cache_resource
def load_model(model_path="models/yolo11_dog_breed.pt"):
    return YOLO(model_path)


MODEL = load_model("models/best.pt")
