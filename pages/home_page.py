from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "login_logo")
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username: str, password: str):
        username_input = self.get_element(self.USERNAME_INPUT)
        password_input = self.get_element(self.PASSWORD_INPUT)
        login_button = self.get_element(self.LOGIN_BUTTON)

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def verify_page(self, tester):
        tester.assertTrue(self.browser.current_url,
                          "https://www.saucedemo.com")
        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")
        username_input = self.get_element(self.USERNAME_INPUT)
        tester.assertEqual(username_input.get_attribute("placeholder"), "Username")

        password_input = self.get_element(self.PASSWORD_INPUT)
        tester.assertEqual(password_input.get_attribute("placeholder"), "Password")

        login_button = self.get_element(self.LOGIN_BUTTON)
        tester.assertEqual(login_button.get_attribute("value"), "Login")
        
