from .state import GraphState

def retrieve(state: GraphState):
    print("--- RETRIEVING LEGAL DOCUMENTS ---")
    
    # Placeholder: In the full project, this queries ChromaDB
    mock_docs = [
        "Tata Group Vendor Policy: Net 45 days payment terms.",
        "Governing Law: Jurisdiction of Mumbai, India."
    ]
    return {"documents": mock_docs}

def generate(state: GraphState):
    print("--- GENERATING ANSWER ---")
    question = state["question"]
    documents = state.get("documents", [])
    
    context = " | ".join(documents)
    generated_answer = f"Based on the context [{context}], here is the answer to: '{question}'"
    
    return {"answer": generated_answer}