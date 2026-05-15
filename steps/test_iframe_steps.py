from pytest_bdd import given, parsers, scenarios, then, when

from pages.iframe_page import IFramePage

scenarios("../features/iframe.feature")


@given("the user opens the iframe page", target_fixture="current_page")
def open_iframe_page(unauthenticated_page):
    page = IFramePage(unauthenticated_page)
    page.open()
    return unauthenticated_page


@when(parsers.parse('the user replaces the TinyMCE body text with "{text}"'))
def replace_tinymce_body_text(current_page, text):
    IFramePage(current_page).replace_body_text(text)


@then("the TinyMCE toolbar is visible")
def tinymce_toolbar_visible(current_page):
    IFramePage(current_page).expect_toolbar_visible()


@then("the TinyMCE editor body is visible")
def tinymce_body_visible(current_page):
    IFramePage(current_page).expect_editor_body_visible()


@then(parsers.parse('the TinyMCE editor body shows "{text}"'))
def tinymce_body_shows_text(current_page, text):
    IFramePage(current_page).expect_body_text(text)
