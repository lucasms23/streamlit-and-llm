FROM python:3.10-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git build-essential curl cmake python3-dev

# Copiar o requirements.txt antes de instalar
COPY requirements.txt .

    # Instalar dependências Python
RUN pip install -r requirements.txt

# Clona e compila o llama.cpp usando cmake
RUN git clone https://github.com/ggerganov/llama.cpp.git /app/llama.cpp && \
    mkdir -p /app/llama.cpp/build && \
    cd /app/llama.cpp/build && \
    cmake .. && \
    make

# Copiar o código da aplicação
COPY server.py .
COPY run_model.sh .
COPY rag.py .
COPY utils.py .

# Copiar modelos, documentos e índices
COPY models/ ./models/
COPY docs/ ./docs/
COPY embeddings/ ./embeddings/

CMD ["bash", "run_model.sh"]
