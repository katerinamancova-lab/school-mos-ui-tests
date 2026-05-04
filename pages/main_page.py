import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://school.mos.ru/"

    LOGIN_TITLE = "//*[normalize-space()='Вход']"
    LOGIN_BUTTON = "//div[normalize-space()='Войти']"

    HOW_GET_ACCESS_LINK = "//a[contains(., 'Как получить доступ')]"
    ABOUT_PROJECT_LINK = "//*[contains(., 'проекте')]"
    USER_AGREEMENT_LINK = "//*[contains(., 'соглашение')]"

    PARENTS_AND_STUDENTS_GROUP = "//*[contains(., 'Для родителей и учеников')]"
    PARENTS_PHONE = "//a[contains(@href, 'tel:+7 (495) 539-55-55')]"

    EMPLOYEES_GROUP = "//*[contains(., 'Для сотрудников')]"
    EMPLOYEES_PHONE = "//*[contains(., '+7 (495) 539-38-38')]"

    VK_LINK = "//a[contains(@href, 'vk.ru')]"
    OK_LINK = "//a[contains(@href, 'ok.ru')]"

    WRITE_US_BUTTON = "//button[.//*[normalize-space()='Написать нам']]"

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(self.URL)
        self.accept_cookies_if_present()

    @allure.step("Проверить элементы главной страницы из шага 1")
    def check_main_page_basic_elements(self):
        self.should_be_visible(self.LOGIN_TITLE)
        self.should_be_visible(self.LOGIN_BUTTON)

    @allure.step("Проверить элементы главной страницы из шага 2")
    def check_main_page_all_elements(self):
        self.should_be_visible(self.LOGIN_TITLE)
        self.should_be_visible(self.LOGIN_BUTTON)
        self.should_be_visible(self.HOW_GET_ACCESS_LINK)

        self.scroll_to_bottom()

        self.should_be_visible(self.ABOUT_PROJECT_LINK)
        self.should_be_visible(self.USER_AGREEMENT_LINK)

        self.should_be_visible(self.PARENTS_AND_STUDENTS_GROUP)
        self.should_be_visible(self.PARENTS_PHONE)

        self.should_be_visible(self.EMPLOYEES_GROUP)
        self.should_be_visible(self.EMPLOYEES_PHONE)

        self.should_be_visible(self.VK_LINK)
        self.should_be_visible(self.OK_LINK)

        self.should_be_visible(self.WRITE_US_BUTTON)

    @allure.step("Нажать кнопку Войти на главной странице")
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Нажать кнопку Написать нам")
    def click_write_us_button(self):
        self.scroll_to_bottom()
        self.js_click(self.WRITE_US_BUTTON)