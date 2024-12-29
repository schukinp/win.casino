import allure
from selene.api import be, browser, s

from pages.base_page import BasePage


class HomePage(BasePage):

    # Locators

    login_btn = s(".btn-green.size-md.btn")
    lang_select = s('div.select-lang')
    user_avatar = s('.avatar')

    # Methods
    @allure.step("Кликнуть Логин")
    def click_login(self):
        self.login_btn.click()

    def switch_geo(self, geo):
        with allure.step(f"Переключить гео на {geo}"):
            self.lang_select.click()
            s(f'img[src*="{geo}.svg"]').click()

    @allure.step("Проверить, что аватар пользователя отображается")
    def check_user_avatar_visible(self):
        self.user_avatar.should(be.visible)



