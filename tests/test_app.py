import json
from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data

def test_add_route():
    client = app.test_client()
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert b"5" in response.data

def test_multiply_route():
    client = app.test_client()
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert b"20" in response.data

def test_get_users():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) == list
    assert len(data) >= 2

def test_create_user():
    client = app.test_client()
    response = client.post("/users", json={"name": "Charlie", "age": 28})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["name"] == "Charlie"
    assert data["age"] == 28
