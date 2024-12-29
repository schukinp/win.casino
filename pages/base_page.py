import allure
from selene.api import browser, be, s
from time import sleep

class BasePage:

    # Locators

    loader = s(".preloader")

    # Methods

    @allure.step("Открыть url")
    def open_url(self, url):
        browser.open(url)
        self.loader.should(be.not_.visible)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_tab(self):
        sleep(3)
        browser.driver().switch_to.window(browser.driver().window_handles[1])

    def check_url_contains(self, url):
        with allure.step(f"Проверить, что в url содержится url {url}"):
            sleep(1)
            browser.driver.current_url.endswith(url)