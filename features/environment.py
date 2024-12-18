from playwright.sync_api import sync_playwright

def before_all(context):
    # Start Playwright and launch browser
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()  # Initialize context.page here

def after_all(context):
    # Cleanup browser and Playwright session
    context.page.close()
    context.browser.close()
    context.playwright.stop()