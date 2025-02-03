import pytest
from app.main import app  # Correctly import the 'app' instance from 'main.py'

@pytest.fixture
def client():
    app.config["TESTING"] = True  # Set the Flask app to testing mode
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')  # Make a request to the '/health' endpoint
    assert response.status_code == 200
    assert response.json == {"status": "ok"}  # Validate the response
