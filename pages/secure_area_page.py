from playwright.sync_api import expect


class SecureAreaPage:
    PATH = "/secure"

    def __init__(self, page):
        self.page = page
        self.heading = page.locator("div.example h2")
        self.flash_banner = page.locator("#flash")
        self.logout_button = page.locator("a.button.secondary.radius")

    def expect_loaded(self):
        self.page.wait_for_url("**/secure")
        expect(self.heading).to_have_text("Secure Area")
        expect(self.logout_button).to_be_visible()

    def open_directly(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")

    def logout(self):
        self.logout_button.click()

    def flash_text(self) -> str:
        expect(self.flash_banner).to_be_visible()
        return " ".join(self.flash_banner.inner_text().split())
