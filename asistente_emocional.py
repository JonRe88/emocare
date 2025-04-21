# archivo: asistente_emocional.py

import streamlit as st
import openai

# Configura tu clave de API
openai.api_key = "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"

st.set_page_config(page_title="Asistente Emocional", page_icon="🌿")
st.title("🌿 Asistente de Apoyo Emocional")
st.markdown("_Hola, estoy aquí para escucharte. Cuéntame, ¿cómo te sientes hoy?_")

# Mantenemos el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe aquí tu mensaje..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Enviar a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente emocional, amable, empático y cálido. Escucha con atención, ofrece consuelo, nunca juzgues. No des consejos médicos, pero sugiere actividades positivas y recordatorios de que la ayuda profesional es valiosa."}
        ] + st.session_state.messages
    )

    reply = response.choices[0].message.content.strip()
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

