import allure
from locators.base_page_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    
    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click_element(HomePageLocators.COOKIE_ACCEPT)
    
    @allure.step('Кликнуть на кнопку заказа вверху')
    def click_top_order_button(self):
        self.click_element(HeaderLocators.ORDER_BUTTON_TOP)
    
    @allure.step('Кликнуть на кнопку заказа внизу')
    def click_bottom_order_button(self):
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(HomePageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step('Кликнуть на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.YANDEX_LOGO)
    
    @allure.step('Кликнуть на логотип Самокат')
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.SCOOTER_LOGO)
    
    @allure.step('Получить ответ на FAQ вопрос')
    def get_faq_answer(self, question_index):
        self.scroll_to_element(HomePageLocators.FAQ_SECTION)
        self.click_element(HomePageLocators.FAQ_QUESTIONS[question_index])
        return self.get_text(HomePageLocators.FAQ_ANSWERS[question_index])
    