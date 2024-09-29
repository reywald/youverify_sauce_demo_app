import json
import time
import unittest

from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class SauceDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("data/items.json", "r") as json_file:
            cls.items_data = json.loads(json_file.read())

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
        inventory_page.add_item_to_cart(self.items_data[0]["name"])
        inventory_page.open_cart()

        cart_page = CartPage(self.browser)
        cart_page.verify_page(self)
        cart_page.check_added_item(self, self.items_data[0])
        cart_page.checkout()

        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
