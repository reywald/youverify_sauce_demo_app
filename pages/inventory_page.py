from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
        self.PRODUCTS = (By.CLASS_NAME, "inventory_item")
        self.SHOPPING_CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")

    def add_random_item_to_cart(self):
        """
        Add a random item to cart
        """
        add_cart_buttons = self.get_elements(
            (By.CSS_SELECTOR, "button[id*='add-to-cart']"))
        size = len(add_cart_buttons)
        from random import randint

        add_cart_buttons[randint(0, size-1)].click()

        cart_number = self.get_element(self.SHOPPING_CART_NUMBER)
        assert cart_number.text == "1"

    def add_item_to_cart(self, item_name: str):
        """
        Search and add an item to cart

        Params
        ------
        item_name: str. The item to search for
        """
        search_item = item_name.lower().replace(" ", "-")

        add_cart_button = self.get_element(
            (By.CSS_SELECTOR, f"button[id*='add-to-cart-{search_item}']"))
        add_cart_button.click()

        cart_number = self.get_element(self.SHOPPING_CART_NUMBER)
        assert cart_number.text == "1"

    def cart_is_empty(self):
        """
        Check that the cart has been emptied after removal or checkout
        """
        cart_number = None
        try:
            cart_number = self.get_element(self.SHOPPING_CART_NUMBER)
        except TimeoutException:
            assert cart_number is None

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
