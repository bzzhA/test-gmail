from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, '//*[@type="email"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]//input[@type="password"]')
    NEXT_BUTTON = (By.XPATH, "//span[contains(text(), 'Далее')]")
