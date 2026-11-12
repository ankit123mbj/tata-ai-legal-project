from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    # Using a lightweight, open-source embedding model suitable for legal text
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")