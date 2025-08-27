import pytest
from playwright.sync_api import sync_playwright

WEB_LOGIN = "https://www.saucedemo.com/"   
API_LOGIN = "https://reqres.in/api"
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()