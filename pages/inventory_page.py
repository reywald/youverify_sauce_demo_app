from selenium.webdriver.common.by import By

from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
        self.PRODUCTS = (By.CLASS_NAME, "inventory_item")

    def add_item_to_cart(self):
        pass

    def open_cart(self):
        """
        Clicks the cart icon to navigate to the cart page
        """
        cart_button = self.get_element(self.CART_LINK)
        cart_button.click()

    def verify_page(self, tester):
        tester.assertIn("inventory.html", self.browser.current_url,
                        "Page URL does not match")

        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")

        page_title = self.get_element(self.PAGE_TITLE)
        tester.assertEqual(page_title.text, "Products",
                           "Page title is not matched")

        cart_link = self.get_element(self.CART_LINK)
        tester.assertIsNotNone(cart_link, "Shopping cart does not exist")

        products = self.get_elements(self.PRODUCTS)
        tester.assertEqual(len(products), 6,
                           "Product Items are not complete")
