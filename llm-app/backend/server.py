from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from rag import build_or_load_index, search


index, documents = build_or_load_index()

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: Prompt):
    try:
        context = search(prompt.text, index, documents)[0]
        prompt_with_context = f"Use o contexto abaixo para responder:\n\n{context}\n\nPergunta: {prompt.text}"

        result = subprocess.run(
            [
                '/app/llama.cpp/build/bin/llama-cli',
                '-m', '/app/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
                '-p', prompt_with_context,
                '-n', '128'
            ],
            capture_output=True, text=True, check=True
        )
        return {"response": result.stdout}
    except subprocess.CalledProcessError as e:
        print("Erro ao rodar o modelo:")
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)
        return {"error": "Erro ao executar o modelo", "details": e.stderr}
