from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class SideBarFragment(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.LOGOUT = (By.ID, "logout_sidebar_link")

    def logout(self):
        """
        Log out of the application
        """
        logout_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.LOGOUT))
        logout_button.click()

    def verify_page(self, tester):
        logout_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.LOGOUT))
        tester.assertIsNotNone(logout_button, "Logout button does not exist")
