import allure
from pages.base_page import BasePage


class FeedbackPage(BasePage):
    TITLE = "//div[contains(@class, 'form-block_title') and contains(normalize-space(), 'Сообщение в техническую поддержку')]"
    CONTINUE_BUTTON = "//button[@data-command='FosConfirmRegion' and normalize-space()='Продолжить']"

    REGION_TEXT = "//*[contains(normalize-space(), 'Пожалуйста, подтвердите ваш регион')]"
    MOSCOW_REGION = "//*[contains(@id, 'select2-fos_regionid') and normalize-space()='Москва']"

    PROBLEM_DROPDOWN = "//*[contains(@id, 'select2-problemid') and contains(normalize-space(), 'Выберите проблему')]"

    SCHOOL_OPTION = "//li[@role='treeitem' and normalize-space()='Школа']"
    COLLEGE_OPTION = "//li[@role='treeitem' and normalize-space()='Колледж']"
    CULTURE_OPTION = "//li[@role='treeitem' and contains(normalize-space(), 'Департамент культуры')]"

    SELECTED_SCHOOL = "//*[contains(@id, 'select2-problemid') and normalize-space()='Школа']"

    @allure.step("Проверить, что открылась форма обратной связи")
    def check_feedback_page_opened(self):
        self.should_be_visible(self.TITLE)
        self.should_be_visible(self.REGION_TEXT)
        self.should_be_visible(self.MOSCOW_REGION)
        self.should_be_visible(self.CONTINUE_BUTTON)

    @allure.step("Нажать кнопку Продолжить")
    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    @allure.step("Проверить, что появился элемент Выберите проблему")
    def check_problem_dropdown_visible(self):
        self.should_be_visible(self.PROBLEM_DROPDOWN)

    @allure.step("Открыть список причин")
    def open_problem_dropdown(self):
        self.click(self.PROBLEM_DROPDOWN)

    @allure.step("Проверить, что появился список причин")
    def check_problem_options_visible(self):
        self.should_be_visible(self.SCHOOL_OPTION)
        self.should_be_visible(self.COLLEGE_OPTION)
        self.should_be_visible(self.CULTURE_OPTION)

    @allure.step("Выбрать причину Школа")
    def select_school_reason(self):
        self.click(self.SCHOOL_OPTION)

    @allure.step("Проверить, что в поле причины появилась надпись Школа")
    def check_school_selected(self):
        self.should_be_visible(self.SELECTED_SCHOOL)