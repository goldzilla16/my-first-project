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
 
