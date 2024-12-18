# pages/login_page.py

# If you see Cannot find reference 'base_page' in '__init__.py'
# The issue might persist due to incorrect package/module path resolution.
# PyCharm sometimes requires manual adjustments to ensure Python can resolve imports correctly.
# Here’s how you can fix it:

# Option 1
# Mark the Root Directory as a Source Root
# 	•	Right-click on the project root folder Python_PyTest_SwagLabs_Framework.
# 	•	Select “Mark Directory as” → “Sources Root”.
#
# This step ensures PyCharm treats the project root as part of the Python path, enabling proper resolution of imports.

# Option 2 Use relative imports within the pages package.
# Change this: from pages.base_page import BasePage To from .base_page import BasePage

from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.fill('input[data-test="username"]', username)
        self.fill('input[data-test="password"]', password)
        self.click('input[data-test="login-button"]')