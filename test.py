import unittest
from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
import time


class SauceDemoTests(unittest.TestCase):

    def setUp(self):
        self.browser = DriverFactory.get_driver("chrome")
        self.browser.get("https://www.saucedemo.com")
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_product_to_cart(self):
        homepage = HomePage(self.browser)
        homepage.verify_page(self)
        homepage.login(username="standard_user", password="secret_sauce")
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
