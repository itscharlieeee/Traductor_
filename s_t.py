import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import openai
import os

st.title("🎧 Traductor por voz en Streamlit")
st.markdown("Graba tu voz, traduce lo que dices y escucha el resultado 🌍")

# Selección de idioma destino
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

st.info("🎙️ Haz clic en 'START' para grabar tu voz")

# Configurar el streamer de audio
webrtc_streamer(
    key="speech",
    mode=WebRtcMode.SENDRECV,
    audio_receiver_size=256,
    media_stream_constraints={"audio": True, "video": False},
)

st.markdown("---")

st.markdown("Por ahora, esta versión graba audio. Para traducirlo automáticamente, necesitaríamos usar una API de transcripción (por ejemplo, Whisper o Google Speech).")

st.info("👉 Si quieres, puedo dejarte el siguiente paso listo para que use Whisper API o Hugging Face y traduzca tu voz automáticamente.")
