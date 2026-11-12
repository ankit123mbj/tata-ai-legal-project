from langchain.tools import tool
from .kb_retriever import search_knowledge_base

@tool
def legal_kb_tool(query: str) -> str:
    """
    Use this tool to search the Tata Group legal knowledge base for 
    clauses regarding audit rights, compliance, confidentiality, etc.
    """
    results = search_knowledge_base(query)
    if not results:
        return "No relevant legal documents found."
    
    return " | ".join(results)