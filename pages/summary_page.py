from selenium.webdriver.common.by import By

from .base_page import BasePage


class SummaryPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.PRODUCT = (By.CLASS_NAME, "cart_item")
        self.ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
        self.FINISH_BUTTON = (By.ID, "finish")
        self.CANCEL_BUTTON = (By.ID, "cancel")

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

        subtotal_price = self.get_element(self.ITEM_TOTAL)
        tester.assertIn(item_details["price"],
                        subtotal_price.text, "Item price does not match")

    def checkout(self):
        """
        Checkout the item in cart
        """
        finish_button = self.get_element(self.FINISH_BUTTON)
        finish_button.click()

    def verify_page(self, tester):
        tester.assertIn("checkout-step-two.html", self.browser.current_url,
                        "Page URL does not match")

        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")

        page_title = self.get_element(self.PAGE_TITLE)
        tester.assertEqual(page_title.text, "Checkout: Overview",
                           "Page title is not matched")

        cancel_button = self.get_element(self.CANCEL_BUTTON)
        tester.assertEqual(cancel_button.text, "Cancel")

        finish_button = self.get_element(self.FINISH_BUTTON)
        tester.assertEqual(finish_button.text, "Finish")
