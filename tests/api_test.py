def test_get_post(api_client):
    # Notice we use api_client.base_url which was attached in the fixture
    response = api_client.get(f"{api_client.base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1


#conftest.py
import pytest
import requests
import os
from dotenv import load_dotenv

# Load variables from .env file (API_URL, API_TOKEN, etc.)
load_dotenv()


def pytest_addoption(parser):
    """Allows you to change environments via command line: pytest --env staging"""
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against: dev, staging, or prod"
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Determines the base URL based on the --env flag or environment variables."""
    env = request.config.getoption("--env")

    # Map environments to URLs (or use a .env default)
    env_urls = {
        "dev": "https://jsonplaceholder.typicode.com",
        "staging": "https://staging-api.example.com",
        "prod": "https://api.example.com"
    }

    # Return the URL for the selected environment
    return os.getenv("BASE_URL", env_urls.get(env))


@pytest.fixture(scope="session")
def api_client(base_url):
    """
    Provides a pre-configured requests session.
    Using a session is faster because it reuses the TCP connection.
    """
    session = requests.Session()

    # Add default headers (like Auth or Content-Type)
    token = os.getenv("API_TOKEN")
    if token:
        session.headers.update({"Authorization": f"Bearer {token}"})

    session.headers.update({"Content-Type": "application/json"})

    # Attach the base_url to the session object for easy access in tests
    session.base_url = base_url

    yield session

    # Clean up after all tests in the session are done
    session.close()


@pytest.fixture
def get_auth_header():
    """Example of a dynamic fixture if you need to refresh tokens per test."""
    return {"Authorization": "Bearer some-dynamic-token"}