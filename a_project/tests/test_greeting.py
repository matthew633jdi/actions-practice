from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)

def test_greeting_status():
    response = client.get("/greeting")
    assert response.status_code == status.HTTP_200_OK

def test_greeting_body():
    response = client.get("/greeting")
    assert response.json() == {'Greeting': 'Wow'}