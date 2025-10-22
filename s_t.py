import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.title("🎙️ Traductor por voz interactivo")

st.markdown("Habla y traduce tu voz en tiempo real 🌍")

idioma_destino = st.selectbox(
    "🌐 Selecciona el idioma destino:",
    {
        "es": "Español 🇪🇸",
        "en": "Inglés 🇺🇸",
        "fr": "Francés 🇫🇷",
        "de": "Alemán 🇩🇪",
        "it": "Italiano 🇮🇹",
        "pt": "Portugués 🇧🇷"
    }
)

if st.button("🎤 Grabar y traducir"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙️ Hable ahora... (esperando tu voz)")
        audio = recognizer.listen(source)

        try:
            st.info("🧠 Reconociendo voz...")
            texto = recognizer.recognize_google(audio, language="es-ES")
            st.success(f"Texto detectado: {texto}")

            st.info("🌐 Traduciendo...")
            traduccion = GoogleTranslator(source="auto", target=idioma_destino).translate(texto)
            st.subheader("🪄 Traducción:")
            st.success(traduccion)

            # Convertir a audio
            tts = gTTS(traduccion, lang=idioma_destino)
            tts.save("traduccion.mp3")
            st.audio("traduccion.mp3", format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Ocurrió un error: {e}")
