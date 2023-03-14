from selenium.webdriver.common.by import By


class MailBoxLocators:
    WRITE_EMAIL_BUTTON = (By.XPATH, "//div[contains(text(), 'Написать')]")
    WHOM_INPUT = (By.XPATH, "//div[@aria-label='Строка поиска']//div//input")
    SUBJECT_INPUT = (By.XPATH, "//input[@name='subjectbox']")
    TEXT_EMAIL = (By.XPATH, "//div[@aria-label='Текст письма']")
    SEND_EMAIL_BUTTON = (By.XPATH, "//div[@aria-label='Отправить ‪(⌘Enter)‬']")
    INBOX_BUTTON = (By.XPATH, '//a[contains(text(), "Входящие")]')
    SUBJECT = (By.XPATH, '//*[contains(text(), "Simba Test")]')
    SELECT_CHECKBOX = (By.XPATH, "//span[@role='checkbox']")
    DELETE_MESSAGE = (By.XPATH, "//div[@aria-label='Удалить']")
