from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    """Test the main endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Fast API!"}


def test_read_docs():
    """Test the docs endpoint"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_read_redoc():
    """Test the redoc endpoint"""
    response = client.get("/redoc")
    assert response.status_code == 200
