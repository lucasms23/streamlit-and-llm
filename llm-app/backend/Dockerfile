FROM python:3.10-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git build-essential curl cmake python3-dev

# Instalar dependências Python
RUN pip install fastapi uvicorn

# Clona e compila o llama.cpp usando cmake
RUN git clone https://github.com/ggerganov/llama.cpp.git /app/llama.cpp && \
    mkdir -p /app/llama.cpp/build && \
    cd /app/llama.cpp/build && \
    cmake .. && \
    make


# Copia o código da API
COPY server.py .
COPY run_model.sh .
COPY models/ ./models/

CMD ["bash", "run_model.sh"]
