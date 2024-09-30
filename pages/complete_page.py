from selenium.webdriver.common.by import By

from .base_page import BasePage


class CompletePage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.IMAGE = (By.CLASS_NAME, "pony_express")
        self.SALUTATION = (By.CLASS_NAME, "complete-header")
        self.BACK = (By.ID, "back-to-products")

    def back_home(self):
        """
        Return to products list page
        """
        back_button = self.get_element(self.BACK)
        self.browser.execute_script("arguments[0].click();", back_button)

    def verify_page(self, tester):
        tester.assertIn("checkout-complete.html", self.browser.current_url,
                        "Page URL does not match")

        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")

        page_title = self.get_element(self.PAGE_TITLE)
        tester.assertEqual(page_title.text, "Checkout: Complete!",
                           "Page title is not matched")

        image_element = self.get_element(self.IMAGE)
        tester.assertTrue(image_element.is_displayed())

        salute_message = self.get_element(self.SALUTATION)
        tester.assertEqual(salute_message.text, "Thank you for your order!")

        back_button = self.get_element(self.BACK)
        tester.assertEqual(back_button.text, "Back Home")
