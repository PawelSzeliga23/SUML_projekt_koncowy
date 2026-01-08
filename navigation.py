import streamlit as st
from streamlit_option_menu import option_menu
import utils.colors as colors
import utils.navigation_utils as nav_utils
import photo_detection

def navigation(selected = None):
    with st.sidebar:
        #st.image("logo.jpg")
        selected = option_menu(
            menu_title="PsiLook",
            options=list(nav_utils.PAGES.keys()),
            icons=list(nav_utils.PAGES.items()),
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
            st.title("Kamera")
        case "Filmy":
            st.title("Filmy")
        case "Zdjęcia":
            photo_detection.photo_detection()
