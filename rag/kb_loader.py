import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from create_embeddings import get_embedding_model

# Paths relative to the 'rag' folder
KB_DIR = "../knowledge_base"
DB_DIR = "../vector_store/chroma_db"

def load_knowledge_base():
    print("--- 1. Loading legal documents from knowledge_base/ ---")
    loader = DirectoryLoader(KB_DIR, glob="*.md", loader_cls=TextLoader)
    documents = loader.load()

    if not documents:
        print("Error: No markdown files found. Check your knowledge_base folder.")
        return

    print(f"--- 2. Chunking {len(documents)} documents ---")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    print(f"--- 3. Creating vector embeddings for {len(chunks)} chunks ---")
    embeddings = get_embedding_model()
    
    # Generate embeddings and save to disk
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print("\nSUCCESS: Vector database built and saved to 'vector_store/chroma_db'")

if __name__ == "__main__":
    load_knowledge_base()