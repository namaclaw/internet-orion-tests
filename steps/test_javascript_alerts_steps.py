from pytest_bdd import given, parsers, scenarios, then, when

from pages.javascript_alerts_page import JavaScriptAlertsPage

scenarios("../features/javascript_alerts.feature")


@given("the user opens the JavaScript alerts page", target_fixture="current_page")
def open_javascript_alerts_page(unauthenticated_page):
    page = JavaScriptAlertsPage(unauthenticated_page)
    page.open()
    return unauthenticated_page


@when("the user accepts the JavaScript alert")
def accept_javascript_alert(current_page):
    JavaScriptAlertsPage(current_page).trigger_alert_accept()


@when("the user dismisses the JavaScript confirm")
def dismiss_javascript_confirm(current_page):
    JavaScriptAlertsPage(current_page).trigger_confirm_dismiss()


@when(parsers.parse('the user submits "{text}" to the JavaScript prompt'))
def submit_javascript_prompt(current_page, text):
    JavaScriptAlertsPage(current_page).trigger_prompt_submit(text)


@then(parsers.parse('the JavaScript alerts result shows "{expected}"'))
def javascript_alerts_result(current_page, expected):
    JavaScriptAlertsPage(current_page).expect_result(expected)
