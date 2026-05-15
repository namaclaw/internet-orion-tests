from playwright.sync_api import expect


class AddRemoveElementsPage:
    PATH = "/add_remove_elements/"

    def __init__(self, page):
        self.page = page
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_buttons = page.get_by_role("button", name="Delete")

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")
        expect(self.add_button).to_be_visible()

    def add_elements(self, count: int):
        for _ in range(count):
            self.add_button.click()

    def remove_elements(self, count: int):
        for _ in range(count):
            self.delete_buttons.nth(0).click()

    def expect_delete_count(self, count: int):
        expect(self.delete_buttons).to_have_count(count)
