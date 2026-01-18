import requests
import pytest

@pytest.mark.api
def test_login_success(base_url, creds):
    r = requests.post(f"{base_url}/api/login", json=creds)
    assert r.status_code == 200
    assert r.json().get("token") == "demo-token"

@pytest.mark.api
def test_login_failure(base_url, creds):
    r = requests.post(
        f"{base_url}/api/login",
        json={"username": creds["username"], "password": "wrong"},
    )
    assert r.status_code == 401