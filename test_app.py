import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index_default(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello " in response.data  

def test_index_injection(client):
    response = client.get("/?name=test") 
    assert b"Hello test" in response.data

def test_fetch_mocked(monkeypatch, client):
    class MockResponse:
        text = "mocked response"

    def mock_get(url, verify):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = client.get("/fetch?url=http://example.com")
    assert response.status_code == 200
    assert b"mocked response" in response.data
