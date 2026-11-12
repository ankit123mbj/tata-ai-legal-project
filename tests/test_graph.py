# Assuming your graph state is defined in graph/state.py
def test_graph_state_structure():
    # Mocking the state that moves through your LangGraph nodes
    mock_state = {
        "question": "What is the governing law?", 
        "documents": ["Jurisdiction of Mumbai"], 
        "answer": ""
    }
    
    assert mock_state["question"] == "What is the governing law?"
    assert len(mock_state["documents"]) == 1
    assert mock_state["answer"] == ""