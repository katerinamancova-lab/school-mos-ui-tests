# UI Autotests for school.mos.ru

Автотесты для тестового задания на Python + Selenium + Pytest.

## Что реализовано

- Page Object Model
- XPath локаторы
- Проверка 8 шагов из ТЗ
- Негативная авторизация
- Проверка формы обратной связи
- Allure отчет

## Технологии

- Python
- Selenium WebDriver
- Pytest
- Allure
- WebDriver Manager

## Структура проекта

```text
pages/
  base_page.py
  main_page.py
  login_page.py
  feedback_page.py

tests/
  test_main.py

conftest.py
pytest.ini
requirements.txt