from selenium.webdriver.common.by import By

from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.HEADING = (By.CLASS_NAME, "app_logo")
        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.FIRSTNAME_INPUT = (By.ID, "first-name")
        self.LASTNAME_INPUT = (By.ID, "last-name")
        self.POSTALCODE_INPUT = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")
        self.CANCEL_BUTTON = (By.ID, "cancel")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def fill_address(self, address_details):
        """
        Add address details in the form
        """
        firstname_input = self.get_element(self.FIRSTNAME_INPUT)
        firstname_input.send_keys(address_details["firstname"])

        lastname_input = self.get_element(self.LASTNAME_INPUT)
        lastname_input.send_keys(address_details["lastname"])

        postalcode_input = self.get_element(self.POSTALCODE_INPUT)
        postalcode_input.send_keys(address_details["postcode"])

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

        self.logger.info(f"{__class__}: Filled Shipping address form")

    def verify_page(self, tester):
        tester.assertIn("checkout-step-one.html", self.browser.current_url,
                        "Page URL does not match")

        heading = self.get_element(self.HEADING)
        tester.assertEqual(heading.text, "Swag Labs",
                           "Page heading is not matched.")

        page_title = self.get_element(self.PAGE_TITLE)
        tester.assertEqual(page_title.text, "Checkout: Your Information",
                           "Page title is not matched")

        firstname_input = self.get_element(self.FIRSTNAME_INPUT)
        tester.assertEqual(firstname_input.get_attribute(
            "placeholder"), "First Name")

        lastname_input = self.get_element(self.LASTNAME_INPUT)
        tester.assertEqual(lastname_input.get_attribute(
            "placeholder"), "Last Name")

        postalcode_input = self.get_element(self.POSTALCODE_INPUT)
        tester.assertEqual(postalcode_input.get_attribute(
            "placeholder"), "Zip/Postal Code")

        cancel_button = self.get_element(self.CANCEL_BUTTON)
        tester.assertEqual(cancel_button.text, "Cancel")

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        tester.assertEqual(continue_button.get_attribute("value"), "Continue")

        self.logger.info(f"{__class__}: Verified the presence of web elements")
