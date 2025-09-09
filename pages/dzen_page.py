import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators

class DzenPage(BasePage):
    
    @allure.step('Проверить редирект на Дзен')
    def is_redirected_to_dzen(self):
        """Проверяет что произошел редирект на главную страницу Дзена"""
        current_url = self.get_current_url()
        return "dzen.ru" in current_url
    