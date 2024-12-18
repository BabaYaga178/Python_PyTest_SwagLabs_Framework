# pages/base_page.py

from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()