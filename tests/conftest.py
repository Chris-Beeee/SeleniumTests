import pytest
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver

# Load variables from .env file
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

    env_urls = {
        "dev": os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com"),
        "staging": "https://staging-api.example.com",
        "prod": "https://api.example.com"
    }

    return env_urls.get(env)


@pytest.fixture(scope="session")
def api_client(base_url):
    """Provides a pre-configured requests session."""
    session = requests.Session()

    token = os.getenv("API_TOKEN")
    if token:
        session.headers.update({"Authorization": f"Bearer {token}"})

    session.headers.update({"Content-Type": "application/json"})
    session.base_url = base_url

    yield session
    session.close()


@pytest.fixture(scope="function")
def driver():
    """Setup the Selenium WebDriver for Chrome."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # In CI, we usually want to run headless
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()
