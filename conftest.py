import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def create_browser():
    """Настройки браузера"""
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
  #  options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.driver_options = options
    browser.config.timeout = 10
    return browser


@pytest.fixture()
def browser_setup():
    """Фикстура сетапа браузера"""
    create_browser()
    yield
    browser.quit()


def pytest_make_parametrize_id(val):
    return repr(val)
