from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator):
        self.wait_for_element(locator).click()
    
    def enter_text(self, locator, text):
        self.wait_for_element(locator).send_keys(text)
    
    def get_text(self, locator):
        return self.wait_for_element(locator).text
    
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def switch_to_new_tab(self):
        """Переключается на новую вкладку"""
        # Ждем пока откроется новая вкладка
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def get_current_url(self):
        return self.driver.current_url
    
    def get_window_handles_count(self):
        """Возвращает количество открытых окон/вкладок"""
        return len(self.driver.window_handles)
    