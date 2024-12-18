# pages/product_page.py

from pages.base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self, product_name: str):
        self.click(f'button[data-test="add-to-cart-{product_name}"]')

    def go_to_cart(self):
        self.click('a[class="shopping_cart_link"]')