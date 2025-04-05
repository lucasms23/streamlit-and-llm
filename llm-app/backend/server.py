from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: Prompt):
    try:
        result = subprocess.run(
            [
                '/app/llama.cpp/build/bin/llama-cli',
                '-m', '/app/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
                '-p', prompt.text,
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
