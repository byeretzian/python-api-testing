import pytest
from src.api import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_with_valid_request(client):
    response = client.post(
        "/get-string-length", json={"body": "This is a test string."}
    )
    assert response.status_code == 200
    assert response.json["length"] == 22


def test_with_no_request_body(client):
    response = client.post("/get-string-length")
    assert response.status_code == 400
    assert response.json == {"error": "No request body."}


def test_with_non_string_request_body(client):
    response = client.post("/get-string-length", json={"body": 23})
    assert response.status_code == 400
    assert response.json == {"error": "The request body must be a string."}
