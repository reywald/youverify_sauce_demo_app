from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class SideBarFragment(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.LOGOUT = (By.ID, "logout_sidebar_link")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def logout(self):
        """
        Log out of the application
        """
        logout_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.LOGOUT))
        logout_button.click()

        self.logger.info(f"{__class__}: Logged out user account")

    def verify_page(self, tester):
        logout_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.LOGOUT))
        tester.assertIsNotNone(logout_button, "Logout button does not exist")

        self.logger.info(f"{__class__}: Verified the presence of web elements")
