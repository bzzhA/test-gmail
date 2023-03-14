from pom.pages.main_page import MainPage
from pom.pages.login_page import LoginPage
from pom.pages.mail_box_page import MailBoxPage


class TestGmail:
    def test_home_page(self, chrome_driver):
        main_page = MainPage(chrome_driver)
        main_page.open_gmail()
        main_page.login_button()

    def test_login_mail(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.paste_email()

    def test_login_password(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.paste_password()

    def test_send_email(self, chrome_driver):
        mail_box = MailBoxPage(chrome_driver)
        for i in range(6):
            mail_box.write_button()
            mail_box.whom_input()
            mail_box.subject_input()
            mail_box.text_email()
            mail_box.send_email()

    def test_check_number_of_email(self, chrome_driver):
        mail_box = MailBoxPage(chrome_driver)
        mail_box.inbox_button()

    def test_check_value_subject(self, chrome_driver):
        mail_box = MailBoxPage(chrome_driver)
        mail_box.subject_value(chrome_driver)

