# streamlit-and-llm

## Arquitetura

+---------------------+         +--------------------+
|  Streamlit Frontend | <---->  |    LLM Backend     |
|     (Container)     |         |    (Container)     |
+---------------------+         +--------------------+
          |                              |
      Usuário                        Modelo 3B


## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- WSL2 habilitado (se possível, para melhor compatibilidade com imagens Linux)
- Modelo `.gguf` compatível com `llama.cpp` (ex: mistral-7b-instruct-v0.1.Q4_K_M.gguf)
- Python 3.10+ no projeto

## Estrutura do Projeto

llm-app/
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── app.py  <-- Streamlit
├── backend/
│   ├── Dockerfile
│   ├── run_model.sh
│   ├── server.py  <-- API que carrega o modelo e responde
│   └── models/    <-- modelo .gguf

## Rodando localmente

1) Baixe o modelo de sua preferencia, por exemplo mistral 7b:

pip3 install huggingface-hub

huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF mistral-7b-instruct-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

2) Coloque o modelo baixado na pasta 'llm-app/backend/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'

3) Execute na raiz llm-app/ o comando:

docker compose up --build

4) Acesse:

Frontend (Streamlit): http://localhost:8501