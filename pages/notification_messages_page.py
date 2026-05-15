from playwright.sync_api import expect


class NotificationMessagesPage:
    PATH = "/notification_message_rendered"
    ALLOWED_MESSAGE_SNIPPETS = (
        "Action successful",
        "Action unsuccesful, please try again",
        "Action unsuccessful, please try again",
    )

    def __init__(self, page):
        self.page = page
        self.trigger_link = page.get_by_role("link", name="Click here")
        self.flash_banner = page.locator("#flash")

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")
        expect(self.trigger_link).to_be_visible()

    def request_new_message(self):
        self.trigger_link.click()

    def expect_banner_visible(self):
        expect(self.flash_banner).to_be_visible()

    def normalized_flash_text(self) -> str:
        self.expect_banner_visible()
        return " ".join(self.flash_banner.inner_text().split())

    def expect_allowed_message_family(self):
        normalized = self.normalized_flash_text()
        assert any(snippet in normalized for snippet in self.ALLOWED_MESSAGE_SNIPPETS), normalized
