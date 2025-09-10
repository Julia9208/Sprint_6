import allure
import pytest
from config.config import TestUsers
from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.feature('Оформление заказа')
class TestOrder:
    
    @pytest.mark.parametrize('user_data,order_button', [
        (TestUsers.USER_1, 'top'),
        (TestUsers.USER_2, 'bottom')
    ], ids=['order_via_top_button', 'order_via_bottom_button'])
    @allure.title('Оформление заказа через разные кнопки')
    @allure.description('Тест оформления заказа с использованием разных кнопок "Заказать"')
    def test_order_via_different_buttons(self, setup_driver, user_data, order_button):
        home_page = HomePage(setup_driver)
        order_page = OrderPage(setup_driver)
        
        home_page.accept_cookies()
        
        if order_button == 'top':
            home_page.click_top_order_button()
        else:
            home_page.click_bottom_order_button()
        
        order_page.complete_order(user_data)
        
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
