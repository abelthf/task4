import pytest
from fastapi import status
from starlette.testclient import TestClient

from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_healt_check(client):
    """
    GIVEN
    WHEN healt check endpoint is called with get method
    THEN response with status 200 and body ok is returned
    """

    response = client.get("/api/health-check/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "OK"}

