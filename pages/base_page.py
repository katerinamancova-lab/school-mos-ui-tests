import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIME_LIMIT = 45

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIME_LIMIT)

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        start_time = time.time()
        self.driver.get(url)
        load_time = time.time() - start_time
        assert load_time <= self.TIME_LIMIT

    @allure.step("Принять cookie, если появилось окно")
    def accept_cookies_if_present(self):
        try:
            cookie_button = self.driver.find_element(
                By.XPATH,
                "//button[contains(., 'Принять') or contains(., 'Согласен') or contains(., 'Хорошо')]"
            )
            cookie_button.click()
        except Exception:
            pass

    def find_visible(self, xpath):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def find_clickable(self, xpath):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def click(self, xpath):
        self.find_clickable(xpath).click()

    def js_click(self, xpath):
        element = self.find_visible(xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def type_text(self, xpath, text):
        element = self.find_visible(xpath)
        element.clear()
        element.send_keys(text)

    def should_be_visible(self, xpath):
        assert self.find_visible(xpath).is_displayed()

    def get_text(self, xpath):
        return self.find_visible(xpath).text

    def get_input_value(self, xpath):
        return self.find_visible(xpath).get_attribute("value")

    def switch_to_new_tab(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def make_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )