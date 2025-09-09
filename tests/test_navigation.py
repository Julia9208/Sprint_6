import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TestConfig
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
        original_window = home_page.driver.current_window_handle
        
        # Кликаем на логотип Яндекс
        home_page.click_yandex_logo()
        
        # Ждем открытия нового окна (явное ожидание вместо time.sleep(2))
        WebDriverWait(home_page.driver, 10).until(
            lambda driver: len(driver.window_handles) == 2
        )
        
        # Проверяем что открылось новое окно
        assert len(home_page.driver.window_handles) == 2, "Не открылось новое окно"
        
        # Переключаемся на новое окно
        home_page.switch_to_new_tab()
        
        # Ждем редиректа на dzen.ru (явное ожидание вместо time.sleep(3))
        WebDriverWait(home_page.driver, 10).until(
            EC.url_contains("dzen.ru")
        )
        
        # Проверяем URL - должен содержать dzen.ru
        current_url = dzen_page.get_current_url()
        assert "dzen.ru" in current_url, f"Ожидался редирект на Дзен, но URL: {current_url}"
        
        # Проверяем что это именно главная страница Дзена
        assert "yredirect=true" in current_url or "/" in current_url, \
            f"Не главная страница Дзена. URL: {current_url}"
        
        # Закрываем вкладку Дзена и возвращаемся обратно
        home_page.driver.close()
        home_page.driver.switch_to.window(original_window)
    
    @allure.title('Проверка перехода на главную через логотип Самокат')
    @allure.description('Проверяем возврат на главную страницу при клике на логотип Самокат')
    def test_scooter_logo_navigation(self, setup_driver):
        home_page = HomePage(setup_driver)
        
        home_page.accept_cookies()
        home_page.click_top_order_button()
        home_page.click_scooter_logo()
        
        current_url = home_page.get_current_url()
        assert current_url == TestConfig.BASE_URL, \
            f"Не произошел переход на главную страницу. Текущий URL: {current_url}"
        