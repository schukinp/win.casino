# Предусловие

- [Python 3.9](https://www.python.org)
- Браузер Chrome
- Драйвер [Chromedriver](https://chromedriver.chromium.org/downloads)

# Установка

`pip install -r requirements.txt`

# Запуск тестов

`pytest tests/`

# Тестовые сценарии
- Успешная регистрация в гео: Bangladesh, India, Spain
- Успешная регистрация c бонус кодом
- Проверка перехода в Телеграм
- Негативные сценарии регистрации: 
    - Пустой email и пароль
    - Неполный email
    - Невалидный email
    - Не отмечен чекбокс Terms of Service: кнопка Регистрации неактивна
    - Уже зарегистрированный email

# Установка allure и просмотр отчета
- Необходимо установить [allure cli](https://github.com/allure-framework/allure2) - раздел Download
- После прогона тестов зайти через терминал в папку allure (`cd tests/allure-results`) и запустить команду `allure serve .`
Отчет автоматически откроется в браузере

# Пример результатов тестов в консоли

```
============================= test session starts ==============================
collecting ... collected 10 items

test_registration.py::TestRegistration::test_registration_success[Bangladesh] 
test_registration.py::TestRegistration::test_registration_success[India] 
test_registration.py::TestRegistration::test_registration_success[Spain] 
test_registration.py::TestRegistration::test_registration_with_bonus_code 
test_registration.py::TestRegistration::test_registration_telegram 
test_registration.py::TestRegistration::test_registration_fail[Empty email and password] 
test_registration.py::TestRegistration::test_registration_fail[email without @] 
test_registration.py::TestRegistration::test_registration_fail[Invalid email] 
test_registration.py::TestRegistration::test_registration_fail[Not marked checkbox - Terms of service] 
test_registration.py::TestRegistration::test_registration_fail[Allready registered email] 

======================== 10 passed in 127.59s (0:02:07) ========================
```

# Структура проекта
- папка `pages` содержит методы и локаторы для работы со страницами
- папка `tests` содержит файл с тестами
- файл `conftest.py` содержит фикстуры для запуска браузера
- файл `pytest.ini` содержит конфиг запуска тестов
- файл `requirements.txt` содержит зависимости проекта
