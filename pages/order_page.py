import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    
    @allure.step('Заполнить информацию о клиенте')
    def fill_customer_info(self, user_data):
        self.enter_text(OrderPageLocators.NAME_FIELD, user_data['name'])
        self.enter_text(OrderPageLocators.LAST_NAME_FIELD, user_data['last_name'])
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, user_data['address'])
        
        self.click_element(OrderPageLocators.METRO_FIELD)
        metro_locator = (OrderPageLocators.METRO_STATION[0], 
                        OrderPageLocators.METRO_STATION[1].format(user_data['metro']))
        self.click_element(metro_locator)
        
        self.enter_text(OrderPageLocators.PHONE_FIELD, user_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step('Заполнить информацию об аренде')
    def fill_rental_info(self, user_data):
        self.enter_text(OrderPageLocators.DELIVERY_DATE, user_data['date'])
        
        self.click_element(OrderPageLocators.RENT_PERIOD)
        rent_option = (OrderPageLocators.RENT_OPTION[0], 
                      OrderPageLocators.RENT_OPTION[1].format('трое суток'))
        self.click_element(rent_option)
        
        self.click_element(OrderPageLocators.COLOR_BLACK)
        self.enter_text(OrderPageLocators.COMMENT_FIELD, user_data['comment'])
        
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
    
    @allure.step('Оформить полный заказ')
    def complete_order(self, user_data):
        self.fill_customer_info(user_data)
        self.fill_rental_info(user_data)
        self.confirm_order()
    
    @allure.step('Проверить успешное оформление заказа')
    def is_order_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)
            )
            return True
        except:
            return False
        