from playwright.sync_api import Page
from tests.conftest import WEB_LOGIN

    
def _get_msg_text(msg):
     # Playwright ConsoleMessage API can expose text() or text attribute depending on version
    try:
        return msg.text
    except Exception:
        try:
            return msg.text()
        except Exception:
            return str(msg)
    

def test_check_console_no_errors(page: Page):
    page.goto(WEB_LOGIN)
    """
    Catch console.error messages during navigation and login flow.
    We collect and assert at the end to keep test teardown stable.
    """
    console_errors = []

    def on_console(msg):
        try:
            if getattr(msg, "type", None) == "error" or getattr(msg, "type", None) == "warning":
                console_errors.append(_get_msg_text(msg))
        except Exception as e:
            # avoid unhandled exceptions inside the event listener
            console_errors.append(f"listener-error: {e}")

    page.goto(WEB_LOGIN)
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    # attach listener before doing anything that could emit console messages
    page.on("console", on_console)
    page.click("input#login-button")

    # final assertion - fail with helpful message if any console errors were captured
    assert not console_errors, f"Console errors found ({len(console_errors)}): {console_errors}"
   
