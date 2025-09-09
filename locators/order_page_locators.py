from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая страница формы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[text()='{}']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая страница формы
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.CLASS_NAME, 'Dropdown-arrow')
    RENT_OPTION = (By.XPATH, "//div[text()='трое суток']")
    COLOR_BLACK = (By.ID, 'black')
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    
    # Подтверждение заказа
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    