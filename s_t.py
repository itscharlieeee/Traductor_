import streamlit as st
from deep_translator import GoogleTranslator

# Configuración de página
st.set_page_config(page_title="Traductor Personalizado", layout="centered")

# Título
st.title("🌍 Traductor Interactivo")
st.write("Introduce el texto, selecciona el idioma y obtén tu traducción al instante.")

# Entrada de texto
texto = st.text_area("✏️ Escribe el texto a traducir:", height=150)

# Selección de idioma destino
idiomas = {
    "Español": "es",
    "Inglés": "en",
    "Francés": "fr",
    "Alemán": "de",
    "Italiano": "it",
    "Portugués": "pt"
}
idioma_destino = st.selectbox("🌐 Selecciona el idioma destino:", list(idiomas.keys()))

# Botón de acción
if st.button("🔄 Traducir"):
    if texto.strip() == "":
        st.warning("Por favor, escribe un texto antes de traducir.")
    else:
        # Traducción
        target_code = idiomas[idioma_destino]
        traducido = GoogleTranslator(source="auto", target=target_code).translate(texto)
        st.subheader("🪄 Traducción:")
        st.success(traducido)
