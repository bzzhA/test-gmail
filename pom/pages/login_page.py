import time

from selenium.webdriver import Keys
from base.base import Base
from pom.locators.login_page_locators import LoginPageLocators


class LoginPage(Base):
    login_locators = LoginPageLocators

    def paste_email(self):
        time.sleep(1)
        self.element_is_visible(self.login_locators.INPUT_EMAIL).send_keys('testpy705@gmail.com')
        self.element_is_visible(self.login_locators.NEXT_BUTTON).click()

    def paste_password(self):
        time.sleep(1)
        self.element_is_visible(self.login_locators.INPUT_PASSWORD).send_keys('Tj5jNaiybpL2ZJf')
        self.element_is_visible(self.login_locators.NEXT_BUTTON).click()
