import allure
import time
from config.urls import Urls
from pages.home_page import HomePage
from pages.dzen_page import DzenPage

@allure.feature('Навигация')
class TestNavigation:
    
    @allure.title('Проверка редиректа на главную страницу Дзена через логотип Яндекс')
    @allure.description('''1. Кликаем на логотип Яндекс
2. Проверяем что открылось новое окно
3. Проверяем редирект на главную страницу Дзена''')
    def test_yandex_logo_redirects_to_dzen(self, setup_driver):
        home_page = HomePage(setup_driver)
        dzen_page = DzenPage(setup_driver)
        
        home_page.accept_cookies()
        
        # Запоминаем текущее окно
        original_window = home_page.current_window_handle()
        
        # Кликаем на логотип Яндекс
        home_page.click_yandex_logo()
        
        # Проверяем что открылось новое окно
        assert home_page.get_window_handles_count() == 2, "Не открылось новое окно"
        
        # Переключаемся на новое окно
        home_page.switch_to_new_tab()

        # Ждем редиректа на dzen.ru
        home_page.wait_for_url_contains("dzen.ru")

        
        # Проверяем URL - должен содержать dzen.ru
        current_url = dzen_page.get_current_url()
        assert "dzen.ru" in current_url, f"Ожидался редирект на Дзен, но URL: {current_url}"
    
    @allure.title('Проверка перехода на главную через логотип Самокат')
    @allure.description('Проверяем возврат на главную страницу при клике на логотип Самокат')
    def test_scooter_logo_navigation(self, setup_driver):
        home_page = HomePage(setup_driver)
        
        home_page.accept_cookies()
        home_page.click_top_order_button()
    
        home_page.click_scooter_logo()
        
        current_url = home_page.get_current_url()
        assert current_url == Urls.BASE_URL, \
            f"Не произошел переход на главную страницу. Текущий URL: {current_url}"
        