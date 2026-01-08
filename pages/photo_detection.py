import streamlit as st
import controllers.photo_controller as photo_controller
import components.dog_card as dog_card


def photo_detection():
    st.title("Wykrywanie rasy psów na zdjęciach")

    uploaded_file = st.file_uploader("Wgraj zdjęcie psa", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

    if uploaded_file is not None:
        col1, col2 = st.columns(2)

        with col1:
            st.image(uploaded_file, caption='Wgrane zdjęcie')
        with col2:
            result = photo_controller.detect_photo(uploaded_file)
            for res in result:
                dog_card.dog_card(res['label'], res['image'], res['confidence'])
