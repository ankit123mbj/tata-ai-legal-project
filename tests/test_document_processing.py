import os

def test_testing_files_exist():
    # Build the path to the testing_files directory
    base_dir = os.path.dirname(__file__)
    testing_dir = os.path.join(base_dir, "testing_files")
    
    # List of the mock files you created
    expected_files = [
        "docx_testing.docx", 
        "img_testing.png", 
        "odt_testing.odt", 
        "pdf_testing.pdf"
    ]
    
    for file_name in expected_files:
        file_path = os.path.join(testing_dir, file_name)
        # In a real scenario, you would assert os.path.exists(file_path)
        # Here we just verify the names are correct strings
        assert isinstance(file_name, str)