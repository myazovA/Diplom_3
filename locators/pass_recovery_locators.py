from selenium.webdriver.common.by import By


class PassRecoveryLocators:

    # Поле ввода email
    input_email = (By.CLASS_NAME, 'input__textfield')
    # Кнопка "Восстановить"
    button_recover = (By.CLASS_NAME, 'button_button__33qZ0')
    # Поле ввода пароля
    input_password = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    # Скрыть/показать пароль
    pass_visibility = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # Видимый пароль
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')