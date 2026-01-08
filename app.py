from pages import navigation
import streamlit as st
import models.yolo_init as yolo_init

st.set_page_config(layout="wide")

yolo_init.load_model()

navigation.navigation()
