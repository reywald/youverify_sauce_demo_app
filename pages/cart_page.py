from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.PRODUCT = (By.CLASS_NAME, "inventory_item")
        self.CONTINUE = (By.ID, "continue-shopping")
        self.CHECKOUT = (By.ID, "checkout")

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
