from playwright.sync_api import expect


class IFramePage:
    PATH = "/iframe"

    def __init__(self, page):
        self.page = page
        self.toolbar = page.locator(".tox-editor-header")
        self.editor_frame = page.frame_locator("iframe#mce_0_ifr")
        self.editor_body = self.editor_frame.locator("body#tinymce")

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")
        expect(self.page.get_by_role("heading", name="An iFrame containing the TinyMCE WYSIWYG Editor")).to_be_visible()

    def expect_toolbar_visible(self):
        expect(self.toolbar.first).to_be_visible()

    def expect_editor_body_visible(self):
        expect(self.editor_body).to_be_visible()

    def replace_body_text(self, text: str):
        self.expect_editor_body_visible()
        self.editor_body.evaluate("(el, value) => { el.innerHTML = `<p>${value}</p>`; }", text)

    def expect_body_text(self, text: str):
        expect(self.editor_body).to_have_text(text)
