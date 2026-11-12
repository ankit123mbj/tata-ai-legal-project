from langchain_community.vectorstores import Chroma
from .create_embeddings import get_embedding_model

DB_DIR = "../vector_store/chroma_db"

def get_vector_store():
    embeddings = get_embedding_model()
    # Connects to the database created by kb_loader.py
    return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)