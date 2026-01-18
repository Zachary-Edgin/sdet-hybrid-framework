import requests
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_health(base_url):
    r = requests.get(f"{base_url}/api/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}