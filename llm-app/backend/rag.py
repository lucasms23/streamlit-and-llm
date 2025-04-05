import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from utils import extract_text_from_pdf

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_or_load_index(doc_dir="docs", index_dir="embeddings"):
    if os.path.exists(f"{index_dir}/index.faiss"):
        index = faiss.read_index(f"{index_dir}/index.faiss")
        with open(f"{index_dir}/docs.pkl", "rb") as f:
            documents = pickle.load(f)
        return index, documents

    documents = []
    embeddings = []

    for filename in os.listdir(doc_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(doc_dir, filename)
            text = extract_text_from_pdf(path)
            documents.append(text)
            embeddings.append(model.encode(text))

    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))

    os.makedirs(index_dir, exist_ok=True)
    faiss.write_index(index, f"{index_dir}/index.faiss")
    with open(f"{index_dir}/docs.pkl", "wb") as f:
        pickle.dump(documents, f)

    return index, documents

def search(query, index, documents, top_k=1):
    query_vector = model.encode([query])
    D, I = index.search(query_vector, top_k)
    return [documents[i] for i in I[0]]
