import pytest
from playwright.sync_api import Page, expect

LOGIN_URL = "https://www.saucedemo.com/"    

@pytest.mark.parametrize("username,password,success", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False)
])
def test_login(page: Page, username, password, success):
    page.goto(LOGIN_URL)
    page.fill("input#user-name", username)
    page.fill("input#password", password)
    page.click("input#login-button")

    if success:
        expect(page.locator(".title")).to_have_text("Products")
    else:
        expect(page.locator("h3[data-test='error']")).to_contain_text("Epic sadface")
