from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    # Раздел "Профиль"
    profile = (By.XPATH, '//a[@href = "/account/profile"]')
    # Раздел "История заказов"
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')
    # Кнопка "Выйти"
    button_logout = (By.XPATH, '//button[@type = "button"]')
    # Кнопка "Зарегистрироваться"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'
    # "В этом разделе вы можете изменить свои персональные данные"
    pers_acc_description = (By.XPATH, '//p[contains(@class, "Account_text")]')