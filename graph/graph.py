from langgraph.graph import StateGraph, START, END
from .state import GraphState
from .nodes import retrieve, generate

# Initialize graph
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

# Define the flow
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the application
app = workflow.compile()