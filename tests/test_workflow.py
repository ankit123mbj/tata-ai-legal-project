from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_api_health():
    # Check if the FastAPI Swagger UI loads successfully
    response = client.get("/docs")
    assert response.status_code == 200

def test_read_items():
    # Check if the database GET endpoint responds correctly
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)