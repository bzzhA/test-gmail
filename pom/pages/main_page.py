from base.base import Base
from pom.locators.main_page_locators import MainPageLocators


class MainPage(Base):
    main_locators = MainPageLocators

    def open_gmail(self):
        self.open()

    def login_button(self):
        self.element_is_visible(self.main_locators.LOGIN_BUTTON).click()
