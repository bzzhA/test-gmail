from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com/gmail/about/'
        # self.url = ''

    def open(self):
        self.driver.get(self.url)
    # def open(self, url: str):
    #     self.driver.get(url)

    def element_is_visible(self, locator, timeout=10) -> WebElement:
        return WAIT(self.driver, timeout).until(EC.visibility_of_element_located(locator))
