from playwright.sync_api import expect


class DynamicLoadingPage:
    def __init__(self, page, path: str):
        self.page = page
        self.path = path
        self.start_button = page.locator("#start button")
        self.loading_indicator = page.locator("#loading")
        self.finish_container = page.locator("#finish")

    def open(self):
        self.page.goto(self.path, wait_until="domcontentloaded")
        expect(self.start_button).to_be_visible()

    def start(self):
        self.start_button.click()

    def wait_for_loading_to_finish(self):
        self.loading_indicator.wait_for(state="hidden", timeout=15000)

    def expect_finish_visible(self):
        expect(self.finish_container).to_be_visible()
        expect(self.finish_container).to_contain_text("Hello World!")
