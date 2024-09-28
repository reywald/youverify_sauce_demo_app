import unittest
from utilities.driver_factory import DriverFactory
import time


class SauceDemoTests(unittest.TestCase):

    def setUp(self):
        self.browser = DriverFactory.get_driver("chrome")
        self.browser.get("https://www.saucedemo.com")
        self.browser.maximize_window()
        time.sleep(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_product_to_cart(self):
        pass


if __name__ == "__main__":
    unittest.main()
