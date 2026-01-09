"""
Webcam detection view for the PsiLook app.
"""

import streamlit as st
from controllers import webcam_controller


def webcam_detection():
    """
    Webcam detection view for the PsiLook app.
    :return:
    """
    result_set = set()
    st.title("Kamera")
    with st.expander("Informacje"):
        st.write("""
        W tej sekcji możesz użyć kamery swojego urządzenia, aby wykryć rasę psa na żywo. 
        Aplikacja wykorzystuje zaawansowany model uczenia maszynowego do analizy obrazu z kamery i 
        identyfikacji rasy psa w czasie rzeczywistym. Wybierz odpowiednią kamerę z listy rozwijanej 
        i kliknij "Uruchom kamerę", aby rozpocząć wykrywanie. Aby zatrzymać transmisję, kliknij "Zatrzymaj kamerę". 
        Powodzenia!
    """)

    col1, col2 = st.columns(2)

    with col1:
        frame_placeholder = st.empty()
        col3, col4, col5, col6 = st.columns(4)

        with col3:
            st.write("Wybierz kamerę :")
        with col4:
            cam_id = st.selectbox("Wybierz kamerę",
                                  options=[0, 1, 2, 3],
                                  index=0,
                                  label_visibility="collapsed")
        with col5:
            start_signal = st.button("Uruchom kamerę")
        with col6:
            stop_signal = st.button("Zatrzymaj kamerę")

    if start_signal:
        webcam_controller.capture_webcam_image(result_set,
                                               cam_id,
                                               stop_signal,
                                               frame_placeholder,
                                               col2)
