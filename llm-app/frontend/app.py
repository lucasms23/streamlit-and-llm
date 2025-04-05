import streamlit as st
import requests

st.title("LLM Expert App 🤖")

user_input = st.text_area("Digite seu prompt")

if st.button("Enviar"):
    with st.spinner("Consultando modelo..."):
        response = requests.post("http://backend:5000/generate", json={"text": user_input})
        if response.status_code == 200:
            st.markdown("### Resposta:")
            st.write(response.json()["response"])
        else:
            st.error("Erro no backend. Status: " + str(response.status_code))
            st.text(response.text)
