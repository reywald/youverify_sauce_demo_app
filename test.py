import json
import time
import unittest

from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.summary_page import SummaryPage
from pages.complete_page import CompletePage


class SauceDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Fetch product items data, billing address data, and login credentials
        """
        with (open("data/items.json", "r") as data_file,
              open("data/address.json", "r") as address_file,
              open("data/creds.json", "r") as cred_file):
            cls.items_data = json.loads(data_file.read())
            cls.address_data = json.loads(address_file.read())
            cls.credentials = json.loads(cred_file.read())

    def setUp(self):
        self.browser = DriverFactory.get_driver("chrome")
        self.browser.get("https://www.saucedemo.com")
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_product_to_cart(self):
        homepage = HomePage(self.browser)
        homepage.verify_page(self)
        homepage.login(
            username=self.credentials["username"], password=self.credentials["password"])

        inventory_page = InventoryPage(self.browser)
        inventory_page.verify_page(self)
        inventory_page.add_item_to_cart(self.items_data[0]["name"])
        inventory_page.open_cart()

        cart_page = CartPage(self.browser)
        cart_page.verify_page(self)
        cart_page.check_added_item(self, self.items_data[0])
        cart_page.checkout()

        checkout_page = CheckoutPage(self.browser)
        checkout_page.verify_page(self)
        checkout_page.fill_address(self.address_data[0])

        summary_page = SummaryPage(self.browser)
        summary_page.verify_page(self)
        summary_page.check_added_item(self, self.items_data[0])
        summary_page.checkout()

        complete_page = CompletePage(self.browser)
        complete_page.verify_page(self)
        complete_page.back_home()

        inventory_page = InventoryPage(self.browser)
        inventory_page.verify_page(self)
        inventory_page.cart_is_empty()

        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
