import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Шаг 3 и 4: форма СУДИР

    TITLE = "//*[normalize-space()='Вход']"

    
    LOGIN_INPUT = "//input[@id='login']"
    PASSWORD_INPUT = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@id='bind']"

    REGISTER_LINK = "//*[contains(text(), 'Зарегистрироваться')]"
    SHOW_PASSWORD = "//*[contains(normalize-space(.), 'Показать пароль')]"
    RESTORE_PASSWORD = "//*[contains(text(), 'Восстановить пароль')]"

    # Социальные сервисы 
    GOSUSLUGI_BUTTON = "//button[@aria-label='Госуслуги']"
    SBER_BUTTON = "//button[@aria-label='Сбербанк']"
    T_BANK_BUTTON = "//button[@aria-label='Т-Банк']"
    VTB_BUTTON = "//button[@aria-label='ВТБ']"
    ALFA_BUTTON = "//button[@aria-label='Альфа-Банк']"

    SHOW_MORE_BUTTON = "//button[contains(normalize-space(), 'Показать ещё')]"

   
    QR_CODE = "//div[@id='qr-code_image']//canvas"

    PHYSICAL_PERSON_INSTRUCTION = "//*[contains(normalize-space(.), 'физических лиц')]"
    LEGAL_PERSON_INSTRUCTION = "//*[contains(normalize-space(.), 'юридических лиц') or contains(normalize-space(.), 'ИП')]"
    TRUSTED_PERSON_INSTRUCTION = "//*[contains(normalize-space(.), 'доверенных лиц')]"

    ERROR_MESSAGE = "//*[contains(text(), 'Введен некорректный логин или пароль')]"

    @allure.step("Проверить, что открылась форма СУДИР")
    def check_login_form_opened(self):
        self.should_be_visible(self.LOGIN_INPUT)
        self.should_be_visible(self.PASSWORD_INPUT)

    @allure.step("Проверить все элементы формы СУДИР по ТЗ")
    def check_login_page_elements(self):
        self.should_be_visible(self.TITLE)

        self.should_be_visible(self.LOGIN_INPUT)
        self.should_be_visible(self.PASSWORD_INPUT)

        self.should_be_visible(self.REGISTER_LINK)
        self.should_be_visible(self.SHOW_PASSWORD)
        self.should_be_visible(self.RESTORE_PASSWORD)

        self.should_be_visible(self.LOGIN_BUTTON)

        self.should_be_visible(self.GOSUSLUGI_BUTTON)
        self.should_be_visible(self.SBER_BUTTON)
        self.should_be_visible(self.T_BANK_BUTTON)
        self.should_be_visible(self.VTB_BUTTON)
        self.should_be_visible(self.ALFA_BUTTON)

        self.should_be_visible(self.SHOW_MORE_BUTTON)
        self.should_be_visible(self.QR_CODE)

        self.should_be_visible(self.PHYSICAL_PERSON_INSTRUCTION)
        self.should_be_visible(self.LEGAL_PERSON_INSTRUCTION)
        self.should_be_visible(self.TRUSTED_PERSON_INSTRUCTION)

    @allure.step("Ввести логин")
    def enter_login(self, login):
        self.type_text(self.LOGIN_INPUT, login)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку Войти в форме СУДИР")
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Ввести логин, пароль и нажать Войти")
    def login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Проверить сообщение об ошибке")
    def check_error_message(self):
        error_text = self.get_text(self.ERROR_MESSAGE)
        assert "Введен некорректный логин или пароль" in error_text

    @allure.step("Проверить, что введённый логин остался в поле")
    def check_login_value(self, expected_login):
        actual_login = self.get_input_value(self.LOGIN_INPUT)
        assert actual_login == expected_login