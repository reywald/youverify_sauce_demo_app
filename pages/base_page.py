from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage(ABC):

    def __init__(self, browser) -> None:
        self.browser = browser

    def get_element(self, web_locator: tuple):
        """
        Checks if a web element exists on the page's DOM

        Params
        ------
        web_locator: a tuple of the form (By.*, "locator")

        Returns
        -------
        web_element: WebElement
        """
        web_element = None

        try:
            web_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(web_locator)
            )
        except TimeoutException as toe:
            toe.msg = f"Could not find element {web_locator} on time"
            raise toe

        return web_element

    def get_elements(self, web_locator: tuple) -> list:
        """
        Checks if multiple web elements exist on the page's DOM

        Params
        ------
        web_locator: a tuple of the form (By.*, "locator")

        Returns
        -------
        web_elements: List[WebElement]
        """
        web_elements = None

        try:
            web_elements = WebDriverWait(self.browser, 100).until(
                EC.presence_of_all_elements_located(web_locator)
            )
        except TimeoutException as toe:
            toe.msg = f"Could not find element {web_locator} on time"
            raise toe

        return web_elements

    @abstractmethod
    def verify_page(self, tester):
        """
        Verifies the web elements of the page

        Params
        ------
        tester: unittest.TestCase instance. Provides assertion methods
        """
