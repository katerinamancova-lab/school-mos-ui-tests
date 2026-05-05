import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feedback_page import FeedbackPage


@allure.feature("school.mos.ru")
@allure.story("E2E ")
def test_school_mos_full_e2e_flow(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    feedback_page = FeedbackPage(driver)

    with allure.step("Шаг 1. Открыть главную страницу"):
        main_page.open_main_page()
        main_page.check_main_page_basic_elements()
        main_page.make_screenshot("Шаг 1. Главная страница")

    with allure.step("Шаг 2. Проверить элементы главной страницы"):
        main_page.check_main_page_all_elements()
        main_page.make_screenshot("Шаг 2. Элементы главной страницы")

    with allure.step("Шаг 3. Открыть форму СУДИР"):
        main_page.click_login_button()
        login_page.check_login_form_opened()
        login_page.make_screenshot("Шаг 3. Форма СУДИР")

    with allure.step("Шаг 4. Проверить элементы формы СУДИР"):
        login_page.check_login_page_elements()
        login_page.make_screenshot("Шаг 4. Элементы формы СУДИР")

    with allure.step("Шаг 5. Авторизация с некорректными данными"):
        login_page.login("81234567890", "QUpoWerm23!")
        login_page.check_error_message()
        login_page.check_login_value("81234567890")
        login_page.make_screenshot("Шаг 5. Ошибка авторизации")

    with allure.step("Шаг 6. Вернуться на главную страницу"):
        main_page.open_main_page()
        main_page.check_main_page_basic_elements()
        main_page.make_screenshot("Шаг 6. Главная страница")

    with allure.step("Шаг 7. Открыть форму обратной связи"):
        main_page.click_write_us_button()
        feedback_page.switch_to_new_tab()
        feedback_page.check_feedback_page_opened()
        feedback_page.make_screenshot("Шаг 7. Форма обратной связи")

    with allure.step("Шаг 8. Заполнить первые шаги формы обратной связи"):
        feedback_page.click_continue_button()
        feedback_page.check_problem_dropdown_visible()

        feedback_page.open_problem_dropdown()
        feedback_page.check_problem_options_visible()

        feedback_page.select_school_reason()
        feedback_page.check_school_selected()

        feedback_page.make_screenshot("Шаг 8. Выбрана причина Школа")