import allure
import pytest
from config.config import TestConfig, TestUsers
from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.feature('Оформление заказа')
class TestOrder:
    
    @allure.title('Оформление заказа через верхнюю кнопку')
    @allure.description('Тест оформления заказа с использованием верхней кнопки "Заказать"')
    def test_order_via_top_button(self, setup_driver):
        home_page = HomePage(setup_driver)
        order_page = OrderPage(setup_driver)
        
        home_page.accept_cookies()
        home_page.click_top_order_button()
        order_page.complete_order(TestUsers.USER_1)
        
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
    
    @allure.title('Оформление заказа через нижнюю кнопку')
    @allure.description('Тест оформления заказа с использованием нижней кнопки "Заказать"')
    def test_order_via_bottom_button(self, setup_driver):
        home_page = HomePage(setup_driver)
        order_page = OrderPage(setup_driver)
        
        home_page.accept_cookies()
        home_page.click_bottom_order_button()
        order_page.complete_order(TestUsers.USER_2)
        
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
        