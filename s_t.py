import streamlit as st
from deep_translator import GoogleTranslator

# Título de la app
st.title("🌍 Traductor Interactivo")

st.markdown("Escribe un texto y elige a qué idioma quieres traducirlo.")

# Entrada de texto
texto = st.text_area("✏️ Escribe el texto aquí:", "")

# Selección del idioma
idioma_destino = st.selectbox(
    "🌐 Selecciona el idioma destino:",
    {
        "es": "Español 🇪🇸",
        "en": "Inglés 🇺🇸",
        "fr": "Francés 🇫🇷",
        "de": "Alemán 🇩🇪",
        "it": "Italiano 🇮🇹",
        "pt": "Portugués 🇧🇷"
    }.values()
)

# Mapeo del idioma seleccionado a su código
idiomas = {
    "Español 🇪🇸": "es",
    "Inglés 🇺🇸": "en",
    "Francés 🇫🇷": "fr",
    "Alemán 🇩🇪": "de",
    "Italiano 🇮🇹": "it",
    "Portugués 🇧🇷": "pt"
}

codigo_destino = [k for k, v in idiomas.items() if v == idioma_destino.split(" ")[0]][0]

# Botón de traducción
if st.button("🔄 Traducir"):
    if texto.strip():
        traduccion = GoogleTranslator(source="auto", target=codigo_destino).translate(texto)
        st.subheader("🪄 Traducción:")
        st.success(traduccion)
    else:
        st.warning("Por favor, escribe un texto antes de traducirlo.")
