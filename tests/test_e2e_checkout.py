from playwright.sync_api import sync_playwright

def test_e2e_checkout():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        context = browser.new_context()
        page = context.new_page()

        # Navigate to SauceDemo website
        page.goto("https://www.saucedemo.com/")

        # Log in
        page.locator('input[data-test="username"]').fill("standard_user")
        page.locator('input[data-test="password"]').fill("secret_sauce")
        page.locator('input[data-test="login-button"]').click()

        # Verify login by checking the presence of the Products header
        assert page.locator('div[class="header_secondary_container"] > span').text_content() == "Products"

        # Add two items to the cart
        page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator('button[data-test="add-to-cart-sauce-labs-bike-light"]').click()

        # Proceed to the cart
        page.locator('a[class="shopping_cart_link"]').click()

        # Verify items in the cart
        cart_items = page.locator('div[class="inventory_item_name"]').all_text_contents()
        assert "Sauce Labs Backpack" in cart_items
        assert "Sauce Labs Bike Light" in cart_items

        # Click on "Checkout"
        page.locator('button[data-test="checkout"]').click()

        # Fill out the checkout information
        page.locator('input[data-test="firstName"]').fill("John")
        page.locator('input[data-test="lastName"]').fill("Doe")
        page.locator('input[data-test="postalCode"]').fill("12345")
        page.locator('input[data-test="continue"]').click()

        # Verify specific Checkout Overview elements
        assert page.locator('div[data-test="payment-info-label"]').is_visible()
        assert page.locator('div[data-test="shipping-info-label"]').is_visible()
        assert page.locator('div[data-test="total-info-label"]').is_visible()

        # Complete the order
        page.locator('button[data-test="finish"]').click()

        # Verify the success message
        success_message = page.locator('h2[class="complete-header"]').text_content()
        assert success_message == "Thank you for your order!"

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_e2e_checkout()