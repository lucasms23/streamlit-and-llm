import streamlit as st
import requests

st.title("LLM Expert App 🤖")

user_input = st.text_area("Digite seu prompt")

if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Por favor, digite um prompt antes de enviar.")
    else:
        with st.spinner("Consultando modelo..."):
            try:
                response = requests.post("http://backend:5000/generate", json={"text": user_input})
                if response.status_code == 200:
                    st.markdown("### Resposta:")
                    st.write(response.json().get("response", "Resposta vazia."))
                else:
                    st.error(f"Erro no backend. Status: {response.status_code}")
                    st.text(f"Detalhes do erro: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error("Erro de conexão com o backend.")
                st.text(str(e))
