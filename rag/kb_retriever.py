from .document_retriever import get_vector_store

def search_knowledge_base(query: str, k: int = 3):
    vector_store = get_vector_store()
    
    # Perform a similarity search in ChromaDB
    results = vector_store.similarity_search(query, k=k)
    
    # Extract and return just the text content
    return [doc.page_content for doc in results]