from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    COOKIE_ACCEPT = (By.ID, 'rcc-confirm-button')
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")
    
    FAQ_QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"), 
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    FAQ_ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"), 
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
