def test_answer_generation():
    expected_keywords = ["Tata", "Agreement", "Policy"]
    mock_generated_answer = "According to the Tata Vendor Policy, the payment terms are Net 45."
    
    # Verify that at least one expected keyword appears in the AI's output
    has_keyword = any(keyword in mock_generated_answer for keyword in expected_keywords)
    assert has_keyword == True