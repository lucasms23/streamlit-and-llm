from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: Prompt):
    result = subprocess.run(
        ['/app/llama.cpp/build/bin/llama', '-m', './models/mistral-7b-instruct-v0.1.Q4_K_M.gguf', '-p', prompt.text, '-n', '128'],
        capture_output=True, text=True
    )
    return {"response": result.stdout}
