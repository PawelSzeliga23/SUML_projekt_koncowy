"""
Navigation sidebar for the PsiLook app.
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils import colors
from utils import navigation_utils as nav_utils
from views import photo_detection
from views import webcam_detection
from views import dog_breed_library
from views import model as model_view


def navigation():
    """
    Navigation sidebar for the PsiLook app.
    :return:
    """
    with st.sidebar:
        selected = option_menu(
            menu_title="PsiLook",
            options=list(nav_utils.PAGES.keys()),
            icons=[nav_utils.PAGES[page] for page in nav_utils.PAGES],
            menu_icon="app-indicator",
            default_index=0,
            styles={
                "nav-link-selected": {"background-color": colors.PRIMARY_COLOR},
            }
        )
    match selected:
        case "Strona główna":
            st.title("Strona główna")
        case "Kamera":
            webcam_detection.webcam_detection()
        case "Filmy":
            st.title("Filmy")
        case "Zdjęcia":
            photo_detection.photo_detection()
        case "Biblioteka ras":
            dog_breed_library.dog_breed_library()
        case "O Modelu":
            model_view.get_model_page()
