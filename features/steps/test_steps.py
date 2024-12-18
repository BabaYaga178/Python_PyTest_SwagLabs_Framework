from behave import given, when, then
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given('I open the SauceDemo website')
def step_open_saucedemo(context):
    context.page.goto("https://www.saucedemo.com/")  # This will now work

@when('I login with "{username}" and "{password}"')
def step_login(context, username, password):
    login_page = LoginPage(context.page)
    login_page.login(username, password)

@when('I add "{product1}" and "{product2}" to the cart')
def step_add_products(context, product1, product2):
    product_page = ProductPage(context.page)
    product_page.add_to_cart(product1)
    product_page.add_to_cart(product2)
    product_page.go_to_cart()

@when('I proceed to checkout and fill the form with "{first_name}", "{last_name}", and "{postal_code}"')
def step_checkout(context, first_name, last_name, postal_code):
    cart_page = CartPage(context.page)
    checkout_page = CheckoutPage(context.page)
    cart_page.checkout()
    checkout_page.fill_checkout_information(first_name, last_name, postal_code)
    checkout_page.finish_order()

@then('I should see "{message}" on the confirmation page')
def step_verify_success(context, message):
    checkout_page = CheckoutPage(context.page)
    success_message = checkout_page.get_success_message()
    assert success_message == message