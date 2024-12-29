# encoding: utf-8


import os

import allure
import pytest
import uuid
from pages.home_page import HomePage
from pages.login_register_modal import LoginRegisterModal

base_url = os.getenv("base_url")


@allure.feature("Регистрация")
@pytest.mark.usefixtures("browser_setup")
class TestRegistration:
    @pytest.mark.parametrize("geo", [
        pytest.param("bn", id="Bangladesh"),
        pytest.param("hi", id="India"),
        pytest.param("es", id="Spain"),
    ])
    def test_registration_success(self, request, geo):

        allure.dynamic.title(f'Успешная регистрация. Geo: {request.node.callspec.id}')

        # тестовые данные

        email = "{}".format(str(uuid.uuid4()))[:8] + "@test.com"
        password = "!Qwerty1"

        page = HomePage()
        page.open_url(base_url + geo)
        page.switch_geo(geo)
        page.click_login()

        page = LoginRegisterModal()
        page.click_register_tab()
        page.register(email=email, password=password)

        page = HomePage()
        page.check_user_avatar_visible()
        
    @allure.title("Успешная регистрация c бонус кодом")
    def test_registration_with_bonus_code(self):
        # тестовые данные

        email = "{}".format(str(uuid.uuid4()))[:8] + "@test.com"
        password = "!Qwerty1"

        page = HomePage()
        page.open_url(base_url)
        page.click_login()

        page = LoginRegisterModal()
        page.click_register_tab()
        page.register(email=email, password=password, bonus="123456")

        page = HomePage()
        page.check_user_avatar_visible()

    @allure.title("Окно авторизации Telegram отображается")
    def test_registration_telegram(self):
        page = HomePage()
        page.open_url(base_url)
        page.click_login()

        page = LoginRegisterModal()
        page.click_register_tab()
        page.click_telegram_btn()
        page.check_url_contains("https://oauth.telegram.org/")

    @pytest.mark.parametrize("email, password, bonus_code, terms_of_service, reg_btn_disabled", [
        pytest.param(" ", " ", None, True, False, id="Empty email and password"),
        pytest.param("test", "!Qwerty1", None, True, False, id="email without @"),
        pytest.param("test@fjjfjs.ert", "!Qwerty1", None, True, False, id="Invalid email"),
        pytest.param("test@test.com", "!Qwerty1", None, False, True, id="Not marked checkbox - Terms of service"),
        pytest.param("e91acee6@test.com", "!Qwerty1", None, True, False, id="Allready registered email"),
    ])
    def test_registration_fail(self, request, email, password, bonus_code, terms_of_service, reg_btn_disabled):

        allure.dynamic.title(f'Негативные сценарии регистрации: {request.node.callspec.id}')


        page = HomePage()
        page.open_url(base_url)
        page.click_login()

        page = LoginRegisterModal()
        page.click_register_tab()
        page.register(email=email,
                      password=password,
                      bonus=bonus_code,
                      terms_of_service=terms_of_service,
                      reg_btn_disabled=reg_btn_disabled)
        if not reg_btn_disabled:
            page.check_validation_error()
