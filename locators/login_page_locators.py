from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка "Восстановить пароль"
    BUTTON_FORGOT_PASSWORD = (By.XPATH, '//a[text() = "Восстановить пароль"]')