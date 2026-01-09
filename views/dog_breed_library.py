"""
Dog breed library view for the PsiLook app.
"""

import streamlit as st
from PIL import Image
from controllers import dog_breed_library_controller


def dog_breed_library():
    """
    Dog breed library view for the PsiLook app.
    This function displays a library of dog breeds with their names and images.
    :return:
    """
    st.title("Biblioteka ras psów")
    with st.expander("Informacje"):
        st.write("""
            W tej sekcji znajdziesz bibliotekę ras psów dostępnych w aplikacji PsiLook. 
            Każda rasa jest przedstawiona z nazwą oraz przykładowym obrazem. 
            Jeśli obraz nie jest dostępny, zostanie wyświetlony domyślny placeholder.
        """)
    with st.spinner("Ładowanie bibliotek ras psów..."):
        breeds_with_images = dog_breed_library_controller.get_all_breads_with_images()

    cols = st.columns(3)
    for index, breed in enumerate(breeds_with_images):
        with cols[index % 3]:
            st.subheader(breed['label'])
            if breed['image'] is None:
                st.image(Image.open("assets/no_image_available.jpg"))
            else:
                st.image(breed['image'])
