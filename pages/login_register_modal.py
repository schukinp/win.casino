import allure
from selene.api import browser, be, s

from pages.base_page import BasePage
from selene.api import ss, query


class LoginRegisterModal(BasePage):

    # Locators

    register_tab = ss(".authorization-tab .simple-tabs__item")[1]
    email_input = s('input[name="email"]')
    password_input = s('input[name="newPassword"]')
    terms_of_service_checkbox = s('label[for="checkbox"]')
    bonus_code_switch = s('div.switch')
    bonus_input = s('div[class*="input-bonus"] input')
    register_login_btn = s('div[class*="email-register email-btn"]')
    close_icon = s('span.authorization__close')
    telegram_btn = s('div.email-auth-social')
    auth_modal = s('div.authorization')
    validation_error = s('.alert.variant-error')

    # Methods
    @allure.step("Кликнуть X чтобы закрыть модальное окно авториазции")
    def click_close_modal_icon(self):
        self.close_icon.click()
        self.auth_modal.should(be.not_.visible)

    @allure.step("Кликнуть Регистрация")
    def click_register_tab(self):
        self.register_tab.click()

    def register(self, email, password, bonus=False, terms_of_service=True, reg_btn_disabled=False):
        with allure.step(f"Зарегистрироваться по email {email}"):
            self.email_input.set(email)
            self.password_input.set(password)
            if bonus:
                self.bonus_code_switch.click()
                self.bonus_input.set(bonus)
            if terms_of_service:
                self.terms_of_service_checkbox.click()
            if not reg_btn_disabled:
                self.register_login_btn.should(be.enabled).click()
            if reg_btn_disabled:
                assert self.register_login_btn.get(query.attribute("disabled"))

    @allure.step("Кликнуть кнопку Telegram")
    def click_telegram_btn(self):
        self.telegram_btn.click()

    def login_as(self, email, password, success=True):
        with allure.step(f"Залогиниться по email {email}"):
            self.email_input.set(email)
            self.password_input.set(password)
            self.register_login_btn.click()
            if success:
                self.register_login_btn.should(be.not_.visible)

    @allure.step("Проверить, что ошибка валидации отображается")
    def check_validation_error(self):
        self.validation_error.should(be.visible)
