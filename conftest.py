import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope='session')
def chrome_driver():
    options_google_browser = ChromeOptions()
    options_google_browser.add_argument('--headless')
    options_google_browser.add_argument('--no-sandbox')
    options_google_browser.add_argument('--disable-gpu')
    options_google_browser.add_argument('--disable-dev-shm-usage')
    options_google_browser.add_argument('--disable-extensions')
    options_google_browser.add_argument('--disable-plugins')
    driver = webdriver.Chrome(options=options_google_browser)
    driver.maximize_window()
    # driver = webdriver.Remote(options=options_google_browser, command_executor='http://localhost:4444/wd/hub')
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def firefox_driver():
    options_mozilla_browser = FirefoxOptions()
    options_mozilla_browser.add_argument('--headless')
    options_mozilla_browser.add_argument('--disable-gpu')
    options_mozilla_browser.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Firefox(options=options_mozilla_browser)
    driver.maximize_window()
    # driver = webdriver.Remote(options=options_mozilla_browser, command_executor='http://localhost:4444/wd/hub')
    yield driver
    driver.quit()
