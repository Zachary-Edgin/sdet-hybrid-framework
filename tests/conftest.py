import os
import time
import requests
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
APP_USERNAME = os.getenv("APP_USERNAME", "demo")
APP_PASSWORD = os.getenv("APP_PASSWORD", "secret")


def wait_for_health(timeout_seconds: int = 30):
    start = time.time()
    while time.time() - start < timeout_seconds:
        try:
            r = requests.get(f"{BASE_URL}/api/health", timeout=2)
            if r.status_code == 200 and r.json().get("status") == "ok":
                return
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError("App did not become healthy in time.")


@pytest.fixture(scope="session", autouse=True)
def ensure_app_is_up():
    wait_for_health()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def creds():
    return {"username": APP_USERNAME, "password": APP_PASSWORD}


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()