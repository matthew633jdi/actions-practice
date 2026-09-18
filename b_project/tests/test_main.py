from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root_status_code():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK

def test_read_root_body():
    response = client.get("/")
    assert response.json() == {"message": "Hi"}
