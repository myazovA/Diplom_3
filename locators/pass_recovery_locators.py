from selenium.webdriver.common.by import By


class PassRecoveryLocators:

    # Поле ввода email
    INPUT_EMAIL = (By.CLASS_NAME, 'input__textfield')
    # Кнопка "Восстановить"
    BUTTON_RECOVER = (By.XPATH, '//button[contains(@class, "button_button")]')
    # Поле ввода пароля
    INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    # Скрыть/показать пароль
    PASS_VISIBILITY = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # Видимый пароль
    VALUE_PASSWORD_IS_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')

