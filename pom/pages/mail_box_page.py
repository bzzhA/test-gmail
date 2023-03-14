import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from base.base import Base
from pom.locators.mail_box_locators import MailBoxLocators


class MailBoxPage(Base):
    mailbox_locators = MailBoxLocators

    def write_button(self):
        self.element_is_visible(self.mailbox_locators.WRITE_EMAIL_BUTTON).click()

    def whom_input(self):
        self.element_is_visible(self.mailbox_locators.WHOM_INPUT).send_keys('testpy705@gmail.com')

    def subject_input(self):
        self.element_is_visible(self.mailbox_locators.SUBJECT_INPUT).send_keys('Simba Test')

    def text_email(self):
        self.element_is_visible(self.mailbox_locators.TEXT_EMAIL).send_keys('Test, Test, Test')

    def send_email(self):
        self.element_is_visible(self.mailbox_locators.SEND_EMAIL_BUTTON).click()

    def inbox_button(self):
        time.sleep(3)
        self.element_is_visible(self.mailbox_locators.INBOX_BUTTON).click()

    def subject_value(self, driver):
        elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Simba Test')]")
        visible_elements = [element for element in elements if
                            element.is_displayed() and
                            element.size['width'] > 0 and
                            element.size['height'] > 0]
        print(f"Количество видимых элементов с темой `Simba test`: {len(visible_elements)}")
