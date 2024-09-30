from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.PRODUCT = (By.CLASS_NAME, "cart_item")
        self.CONTINUE = (By.ID, "continue-shopping")
        self.CHECKOUT = (By.ID, "checkout")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def check_added_item(self, tester, item_details: dict):
        """
        Verify that an item is visible in the cart page

        Params
        ------
        item_details: {"name": str, "price": str}
        """

        cart_item = self.get_element(self.PRODUCT)
        tester.assertIsNotNone(cart_item, "No item in cart")

        item_name = self.get_element((By.CLASS_NAME, "inventory_item_name"))
        tester.assertEqual(
            item_name.text, item_details["name"], "Item name does not match")

        item_price = self.get_element((By.CLASS_NAME, "inventory_item_price"))
        tester.assertEqual(
            item_price.text, item_details["price"], "Item price does not match")
        
        self.logger.info(f"{__class__}: Verified the presence of the added item")

    def checkout(self):
        """
        Checkout the item in cart
        """
        checkout_button = self.get_element(self.CHECKOUT)
        checkout_button.click()

        self.logger.info(f"{__class__}: Checked out the item")

    def verify_page(self, tester):
        tester.assertIn("cart.html", self.browser.current_url,
                        "Page URL does not match")

        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")

        page_title = self.get_element(self.PAGE_TITLE)
        tester.assertEqual(page_title.text, "Your Cart",
                           "Page title is not matched")

        continue_button = self.get_element(self.CONTINUE)
        tester.assertEqual(continue_button.text, "Continue Shopping")

        checkout_button = self.get_element(self.CHECKOUT)
        tester.assertEqual(checkout_button.text, "Checkout")

        self.logger.info(f"{__class__}: Verified the presence of web elements")
