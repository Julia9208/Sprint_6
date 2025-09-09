from selenium.webdriver.common.by import By

class HeaderLocators:
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Статус заказа')]")
    