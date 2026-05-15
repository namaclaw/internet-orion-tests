from pathlib import Path
import json

import pytest
from playwright.sync_api import expect

BASE_URL = "https://the-internet.herokuapp.com"
AUTH_STATE_PATH = Path(__file__).parent / ".auth" / "state.json"
PUBLIC_USERNAME = "tomsmith"
PUBLIC_PASSWORD = "SuperSecretPassword!"
DEFAULT_TIMEOUT_MS = 15000


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "base_url": BASE_URL}


@pytest.fixture(scope="session")
def app_base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def auth_credentials():
    return {
        "username": PUBLIC_USERNAME,
        "password": PUBLIC_PASSWORD,
    }


@pytest.fixture(scope="session")
def auth_state_path():
    AUTH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return AUTH_STATE_PATH


@pytest.fixture(scope="session")
def authenticated_storage_state(browser, auth_credentials, auth_state_path, app_base_url):
    if auth_state_path.exists():
        return str(auth_state_path)

    context = browser.new_context(base_url=app_base_url)
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    page.goto("/login", wait_until="domcontentloaded")
    page.locator("#username").fill(auth_credentials["username"])
    page.locator("#password").fill(auth_credentials["password"])
    page.locator('button[type="submit"]').click()
    page.wait_for_url("**/secure")
    expect(page.locator("#flash")).to_be_visible()
    storage_state = context.storage_state()
    auth_state_path.write_text(json.dumps(storage_state, indent=2))
    context.close()
    return str(auth_state_path)


@pytest.fixture
def unauthenticated_page(browser, app_base_url):
    context = browser.new_context(base_url=app_base_url)
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield page
    context.close()


@pytest.fixture
def authenticated_page(browser, app_base_url, authenticated_storage_state):
    context = browser.new_context(base_url=app_base_url, storage_state=authenticated_storage_state)
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield page
    context.close()
