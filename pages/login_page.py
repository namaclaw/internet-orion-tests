from playwright.sync_api import expect


class LoginPage:
    PATH = "/login"
    SECURE_PATH = "/secure"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')
        self.flash_banner = page.locator("#flash")
        self.heading = page.get_by_role("heading", name="Login Page")

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")
        expect(self.heading).to_be_visible()

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_with_empty_fields(self):
        self.login_button.click()

    def flash_text(self) -> str:
        expect(self.flash_banner).to_be_visible()
        return " ".join(self.flash_banner.inner_text().split())

    def is_displayed(self) -> bool:
        return self.username_input.is_visible() and self.password_input.is_visible()
