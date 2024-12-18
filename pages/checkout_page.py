# pages/checkout_page.py

from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.fill('input[data-test="firstName"]', first_name)
        self.fill('input[data-test="lastName"]', last_name)
        self.fill('input[data-test="postalCode"]', postal_code)
        self.click('input[data-test="continue"]')

    def finish_order(self):
        self.click('button[data-test="finish"]')

    def get_success_message(self) -> str:
        return self.get_text('h2[class="complete-header"]')