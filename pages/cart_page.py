# pages/cart_page.py

from pages.base_page import BasePage

class CartPage(BasePage):
    def verify_item_in_cart(self, item_name: str) -> bool:
        cart_items = self.page.locator('div[class="inventory_item_name"]').all_text_contents()
        return item_name in cart_items

    def checkout(self):
        self.click('button[data-test="checkout"]')