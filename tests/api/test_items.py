from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    """Test creating an item"""
    response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "A test item"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test item"
    assert "id" in data


def test_read_items():
    """Test reading items"""
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_item():
    """Test reading a specific item"""
    # First create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "A test item"}
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    
    # Then read it
    response = client.get(f"/api/v1/items/{created_item['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["id"] == created_item["id"]


def test_update_item():
    """Test updating an item"""
    # First create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "A test item"}
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    
    # Then update it
    update_response = client.put(
        f"/api/v1/items/{created_item['id']}",
        json={"name": "Updated Item", "description": "An updated item"}
    )
    assert update_response.status_code == 200
    updated_item = update_response.json()
    assert updated_item["name"] == "Updated Item"
    assert updated_item["description"] == "An updated item"


def test_delete_item():
    """Test deleting an item"""
    # First create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "A test item"}
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    
    # Then delete it
    delete_response = client.delete(f"/api/v1/items/{created_item['id']}")
    assert delete_response.status_code == 200
    
    # Try to read it again (should fail)
    get_response = client.get(f"/api/v1/items/{created_item['id']}")
    assert get_response.status_code == 404
