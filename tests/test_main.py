import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feedback_page import FeedbackPage


@allure.feature("school.mos.ru")
@allure.story("Шаг 1. Открытие главной страницы")
def test_step_1_open_main_page(driver):
    main_page = MainPage(driver)

    main_page.open_main_page()
    main_page.check_main_page_basic_elements()
    main_page.make_screenshot("Шаг 1. Главная страница")


@allure.feature("school.mos.ru")
@allure.story("Шаг 2. Проверка отображения элементов на главной странице")
def test_step_2_main_page_elements(driver):
    main_page = MainPage(driver)

    main_page.open_main_page()
    main_page.check_main_page_all_elements()
    main_page.make_screenshot("Шаг 2. Элементы главной страницы")


@allure.feature("school.mos.ru")
@allure.story("Шаг 3. Открытие формы СУДИР")
def test_step_3_open_login_form(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open_main_page()
    main_page.click_login_button()

    login_page.check_login_form_opened()
    login_page.make_screenshot("Шаг 3. Форма СУДИР")


@allure.feature("school.mos.ru")
@allure.story("Шаг 4. Проверка элементов на странице СУДИР")
def test_step_4_login_page_elements(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open_main_page()
    main_page.click_login_button()

    login_page.check_login_page_elements()
    login_page.make_screenshot("Шаг 4. Элементы формы СУДИР")


@allure.feature("school.mos.ru")
@allure.story("Шаг 5. Авторизация")
def test_step_5_invalid_authorization(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open_main_page()
    main_page.click_login_button()

    login_page.login("81234567890", "QUpoWerm23!")

    login_page.check_error_message()
    login_page.check_login_value("81234567890")
    login_page.make_screenshot("Шаг 5. Ошибка авторизации")


@allure.feature("school.mos.ru")
@allure.story("Шаг 6. Возвращение на главную страницу")
def test_step_6_return_to_main_page(driver):
    main_page = MainPage(driver)

    main_page.open_main_page()
    main_page.check_main_page_basic_elements()
    main_page.make_screenshot("Шаг 6. Главная страница")


@allure.feature("school.mos.ru")
@allure.story("Шаг 7. Переход в форму обратной связи")
def test_step_7_open_feedback_form(driver):
    main_page = MainPage(driver)
    feedback_page = FeedbackPage(driver)

    main_page.open_main_page()
    main_page.click_write_us_button()

    feedback_page.switch_to_new_tab()
    feedback_page.check_feedback_page_opened()
    feedback_page.make_screenshot("Шаг 7. Форма обратной связи")


@allure.feature("school.mos.ru")
@allure.story("Шаг 8. Заполнение первых двух шагов формы")
def test_step_8_fill_first_steps_feedback_form(driver):
    main_page = MainPage(driver)
    feedback_page = FeedbackPage(driver)

    main_page.open_main_page()
    main_page.click_write_us_button()

    feedback_page.switch_to_new_tab()
    feedback_page.check_feedback_page_opened()

    feedback_page.click_continue_button()
    feedback_page.check_problem_dropdown_visible()

    feedback_page.open_problem_dropdown()
    feedback_page.check_problem_options_visible()

    feedback_page.select_school_reason()
    feedback_page.check_school_selected()

    feedback_page.make_screenshot("Шаг 8. Выбрана причина Школа")