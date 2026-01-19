import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_success(base_url, creds, page):
    page.goto(f"{base_url}/")
    page.fill("#username", creds["username"])
    page.fill("#password", "wrong")
    page.click("#login-btn")

    page.wait_for_url("**/dashboard", timeout=5000)
    assert page.locator("#dashboard-title").inner_text() == "Dashboard"
    assert "Welcome" in page.locator("#welcome").inner_text()

@pytest.mark.ui
def test_ui_login_failure(base_url, page):
    page.goto(f"{base_url}/")
    page.fill("#username", "demo")
    page.fill("#password", "wrong")
    page.click("#login-btn")

    assert page.locator("#error").inner_text() == "Invalid credentials"