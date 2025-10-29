import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Flask CI/CD Demo" in response.data

def test_users_page(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Users List" in response.data

def test_add_user(client):
    # Add a new user
    response = client.post("/users", data={"name": "Charlie", "age": "28"}, follow_redirects=True)
    assert response.status_code == 200
    # Confirm user is in the page
    assert b"Charlie" in response.data
