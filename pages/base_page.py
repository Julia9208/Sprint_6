import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Ожидание элемента {locator}')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step('Клик на элемент {locator}')
    def click_element(self, locator):
        self.wait_for_element(locator).click()
    
    @allure.step('Ввод текста "{text}" в элемент {locator}')
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Получение текста элемента {locator}')
    def get_text(self, locator):
        return self.wait_for_element(locator).text
    
    @allure.step('Скролл к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Закрытие текущей вкладки')
    def close_current_tab(self):
        self.driver.close()
    
    @allure.step('Переключение на окно {window_handle}')
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    @allure.step('Получение количества открытых окон')
    def get_window_handles_count(self):
        return len(self.driver.window_handles)
    
    @allure.step('Ожидание нового окна')
    def wait_for_new_window(self, timeout=10):
        current_handles = self.driver.window_handles
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len(current_handles)
        )
    
    @allure.step('Ожидание URL содержащего {text}')
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
    
    @allure.step('Получение текущего handle окна')
    def current_window_handle(self):
        return self.driver.current_window_handle
    