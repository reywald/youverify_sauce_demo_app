from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from test import test_application_is_reachable, test_application_web_elements

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

APP_URL = "https://d28dp6fycxce58.cloudfront.net/"

test_application_is_reachable(URL=APP_URL, driver=driver)
test_application_web_elements(URL=APP_URL, driver=driver)
