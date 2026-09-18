from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_status():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK

def test_health_body():
    response = client.get("/health")
    assert response.json() == {'Health': 'ok'}