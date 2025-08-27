import pytest
from playwright.sync_api import Page, expect
from tests.conftest import API_LOGIN 

@pytest.mark.api
def test_initial_cookies_empty(page: Page):
    """Verify that the browser context starts with no cookies."""
    page.goto(API_LOGIN)
    cookies = page.context.cookies()
    print(f"Initial cookies: {cookies}")
    assert cookies == [], "Expected no cookies at the start"
    
@pytest.mark.api
def test_add_cookie(page: Page):
    """Verify that a cookie can be added successfully."""
    page.goto(API_LOGIN)
    cookie_data = {
        'name': 'cookie1',
        'value': '123',
        'url': 'https://reqres.in/api'
    }
    page.context.add_cookies([cookie_data])

    cookies = page.context.cookies()
    print(f"Cookies after addition: {cookies}")
    assert any(c['name'] == 'cookie1' and c['value'] == '123' for c in cookies), \
        "Cookie 'cookie1' was not added properly"

@pytest.mark.api
def test_clear_cookies(page: Page):
    """Verify that cookies can be cleared successfully."""
    page.goto(API_LOGIN)
    # Add a cookie first so there is something to clear
    page.context.add_cookies([{'name': 'cookie1', 'value': '123', 'url': 'https://reqres.in/api'}])
    
    page.context.clear_cookies()
    cookies = page.context.cookies()
    print(f"Cookies after clearing: {cookies}")
    assert cookies == [], "Expected cookies to be cleared"
