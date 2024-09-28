import unittest
from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
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

        inventory_page = InventoryPage(self.browser)
        inventory_page.verify_page(self)
        inventory_page.open_cart()
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
