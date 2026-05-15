from playwright.sync_api import expect


class JavaScriptAlertsPage:
    PATH = "/javascript_alerts"

    def __init__(self, page):
        self.page = page
        self.js_alert_button = page.get_by_role("button", name="Click for JS Alert")
        self.js_confirm_button = page.get_by_role("button", name="Click for JS Confirm")
        self.js_prompt_button = page.get_by_role("button", name="Click for JS Prompt")
        self.result = page.locator("#result")

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")
        expect(self.js_alert_button).to_be_visible()

    def trigger_alert_accept(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.js_alert_button.click()

    def trigger_confirm_dismiss(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.js_confirm_button.click()

    def trigger_prompt_submit(self, text: str):
        self.page.once("dialog", lambda dialog: dialog.accept(text))
        self.js_prompt_button.click()

    def expect_result(self, expected: str):
        expect(self.result).to_have_text(expected)
