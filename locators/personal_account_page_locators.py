from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    # Раздел "Профиль"
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')
    # Раздел "История заказов"
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]')
    # Кнопка "Выйти"
    BUTTON_LOGOUT = (By.XPATH, '//button[@type = "button"]')
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = By.XPATH, '//a[text() = "Зарегистрироваться"]'
    # "В этом разделе вы можете изменить свои персональные данные"
    PERS_ACC_DESCRIPTION = (By.XPATH, '//p[contains(@class, "Account_text")]')