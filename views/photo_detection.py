"""
Photo detection view for Streamlit app.
"""
import streamlit as st
import time
from streamlit_option_menu import option_menu
from controllers import photo_controller
from components import dog_card
from utils import colors


def photo_detection():
    """
    Photo detection view for Streamlit app.
    This function allows users to upload a photo or use the camera
    to detect dog breeds in the image.
    :return:
    """
    st.title("Wykrywanie rasy psów na zdjęciach")
    with st.expander("Informacje"):
        st.write("""
            W tej sekcji możesz wgrać zdjęcie psa lub użyć kamery, aby wykryć rasę psa na zdjęciu. 
            Aplikacja wykorzystuje zaawansowany model uczenia maszynowego do analizy obrazu i 
            identyfikacji rasy psa. Po przetworzeniu zdjęcia, aplikacja wyświetli 
            najbardziej prawdopodobne rasy wraz z poziomem pewności. W razie braku wykrycia psa na zdjęciu,
            spróbuj ponownie z innym zdjęciem. Powodzenia!
        """)

    col1, col2 = st.columns(2)

    uploaded_file = None
    camera_file = None

    with col1:
        selected = option_menu(
            menu_title=None,
            options=["Wgraj zdjęcie", "Użyj kamery"],
            icons=["image", "camera"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "nav-link-selected": {"background-color": colors.PRIMARY_COLOR},
            }
        )
        match selected:
            case "Wgraj zdjęcie":
                uploaded_file = st.file_uploader("Wgraj zdjęcie psa", type=["jpg", "jpeg", "png"],
                                                 accept_multiple_files=False)
            case "Użyj kamery":
                camera_file = st.camera_input("Wykryj rasę psa za pomocą zdjęcia")

    input_file = camera_file or uploaded_file

    if input_file is not None:
        with col1:
            if not camera_file:
                st.image(input_file, caption='Wgrane zdjęcie')
        with col2:
            with st.spinner("Trwa wykrywanie rasy psa..."):
                time.sleep(1)
                try:
                    result = photo_controller.detect_photo(input_file)
                except Exception as e:
                    st.error(f"Wystąpił błąd podczas przetwarzania zdjęcia: {e}")
                    return
            if len(result) == 0:
                st.warning("Nie wykryto psa na zdjęciu. Spróbuj ponownie z innym zdjęciem.")
            for res in result:
                dog_card.dog_card(res['label'], res['image'], res['confidence'])
