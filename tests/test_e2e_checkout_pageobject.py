# tests/test_sauce_demo.py

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_e2e_checkout():
    with sync_playwright() as p:
        # Set up browser and context
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Initialize Page Object classes
        login_page = LoginPage(page)
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        # Go to the SauceDemo website
        login_page.go_to("https://www.saucedemo.com/")

        # Perform Login
        login_page.login("standard_user", "secret_sauce")

        # Add products to cart
        product_page.add_to_cart("sauce-labs-backpack")
        product_page.add_to_cart("sauce-labs-bike-light")

        # Go to the cart and verify items
        product_page.go_to_cart()
        assert cart_page.verify_item_in_cart("Sauce Labs Backpack")
        assert cart_page.verify_item_in_cart("Sauce Labs Bike Light")

        # Proceed to checkout
        cart_page.checkout()

        # Fill in checkout details and complete the order
        checkout_page.fill_checkout_information("John", "Doe", "12345")
        checkout_page.finish_order()

        # Verify success message
        success_message = checkout_page.get_success_message()
        assert success_message == "Thank you for your order!"

        # Close the browser
        browser.close()