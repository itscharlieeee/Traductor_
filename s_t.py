import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Traductor Interactivo")
texto = st.text_area("✏️ Escribe el texto a traducir:")

idioma_destino = st.selectbox(
    "🌐 Selecciona el idioma destino:",
    {"es": "Español", "en": "Inglés", "fr": "Francés", "de": "Alemán"}
)

if st.button("Traducir"):
    if texto.strip():
        traduccion = GoogleTranslator(source="auto", target=idioma_destino).translate(texto)
        st.subheader("Traducción:")
        st.success(traduccion)
    else:
        st.warning("Por favor, escribe un texto antes de traducirlo.")
