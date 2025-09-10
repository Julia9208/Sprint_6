from selenium.webdriver.common.by import By

class HeaderLocators:
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ORDER_BUTTON_TOP = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_STATUS_BUTTON = (By.XPATH, ".//button[text()='Статус заказа']")
    