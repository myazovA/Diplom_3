from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка "Восстановить пароль"
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'