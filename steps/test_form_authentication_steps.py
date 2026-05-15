from pytest_bdd import given, scenarios, then, when
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

scenarios("../features/form_authentication.feature")


@given("the user opens the login page", target_fixture="current_page")
def current_page_from_login(unauthenticated_page):
    login_page = LoginPage(unauthenticated_page)
    login_page.open()
    return unauthenticated_page


@given("the user is signed in on the secure area", target_fixture="current_page")
def current_page_signed_in(unauthenticated_page, auth_credentials):
    login_page = LoginPage(unauthenticated_page)
    login_page.open()
    login_page.login(auth_credentials["username"], auth_credentials["password"])
    secure_page = SecureAreaPage(unauthenticated_page)
    secure_page.expect_loaded()
    return unauthenticated_page


@given("the user is unauthenticated", target_fixture="current_page")
def current_page_unauthenticated(unauthenticated_page):
    return unauthenticated_page


@given("the user has an authenticated browser state", target_fixture="current_page")
def current_page_authenticated(authenticated_page):
    return authenticated_page


@when("the user signs in with valid public demo credentials")
def sign_in_with_valid_credentials(current_page, auth_credentials):
    login_page = LoginPage(current_page)
    login_page.login(auth_credentials["username"], auth_credentials["password"])


@when("the user logs out")
def log_out(current_page):
    secure_page = SecureAreaPage(current_page)
    secure_page.logout()


@when("the user signs in with an invalid username")
def sign_in_with_invalid_username(current_page, auth_credentials):
    login_page = LoginPage(current_page)
    login_page.login("invalid-user", auth_credentials["password"])


@when("the user signs in with an invalid password")
def sign_in_with_invalid_password(current_page, auth_credentials):
    login_page = LoginPage(current_page)
    login_page.login(auth_credentials["username"], "incorrect-password")


@when("the user submits the login form with empty fields")
def submit_empty_fields(current_page):
    login_page = LoginPage(current_page)
    login_page.login_with_empty_fields()


@when("the user opens the secure area directly")
def open_secure_directly(current_page):
    secure_page = SecureAreaPage(current_page)
    secure_page.open_directly()


@when("the user opens the secure area directly from authenticated state")
def open_secure_authenticated(current_page):
    secure_page = SecureAreaPage(current_page)
    secure_page.open_directly()


@then("the secure area is displayed")
def secure_area_displayed(current_page):
    secure_page = SecureAreaPage(current_page)
    secure_page.expect_loaded()


@then("a success flash message is shown")
def success_flash(current_page):
    flash_text = LoginPage(current_page).flash_text()
    assert "You logged into a secure area!" in flash_text


@then("the login page is displayed again")
def login_page_displayed_again(current_page):
    login_page = LoginPage(current_page)
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(current_page).to_have_url("https://the-internet.herokuapp.com/login")


@then("a logout flash message is shown")
def logout_flash(current_page):
    flash_text = SecureAreaPage(current_page).flash_text()
    assert "You logged out of the secure area!" in flash_text


@then("the login page remains displayed")
def login_page_remains_displayed(current_page):
    login_page = LoginPage(current_page)
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(current_page).to_have_url("https://the-internet.herokuapp.com/login")


@then("an invalid username flash message is shown")
def invalid_username_flash(current_page):
    flash_text = LoginPage(current_page).flash_text()
    assert "Your username is invalid!" in flash_text


@then("an invalid password flash message is shown")
def invalid_password_flash(current_page):
    flash_text = LoginPage(current_page).flash_text()
    assert "Your password is invalid!" in flash_text


@then("an authentication-required flash message is shown")
def auth_required_flash(current_page):
    flash_text = LoginPage(current_page).flash_text()
    assert "You must login to view the secure area!" in flash_text


@then("the logout control is available")
def logout_control_available(current_page):
    secure_page = SecureAreaPage(current_page)
    expect(secure_page.logout_button).to_be_visible()


@then("the flash message is visible")
def flash_visible(current_page):
    expect(current_page.locator("#flash")).to_be_visible()
