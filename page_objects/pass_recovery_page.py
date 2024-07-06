from locators.pass_recovery_locators import PassRecoveryLocators
from page_objects.base_page import BasePage
from helpers import *
import allure

class PassRecoveryPage(BasePage):

    @allure.step('Проверка отображения поля email')
    def input_email_check(self):
        return self.check_element_visibility(PassRecoveryLocators.INPUT_EMAIL)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PassRecoveryLocators.INPUT_EMAIL)
        email = random_email()
        self.send_keys_to_input(PassRecoveryLocators.INPUT_EMAIL, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PassRecoveryLocators.BUTTON_RECOVER)
        self.click_on_element(PassRecoveryLocators.BUTTON_RECOVER)

    @allure.step('Проверка отображения поля password')
    def check_input_password_visibility(self):
        self.wait_visibility_of_element(PassRecoveryLocators.INPUT_PASSWORD)
        return self.check_element_visibility(PassRecoveryLocators.INPUT_PASSWORD)

    @allure.step('Ввести пароль')
    def send_password(self):
        self.wait_visibility_of_element(PassRecoveryLocators.INPUT_PASSWORD)
        password = random_pass()
        self.send_keys_to_input(PassRecoveryLocators.INPUT_PASSWORD, password)

    @allure.step('Кликнуть на иноку видимости пароля')
    def click_pass_visibility_icon(self):
        self.wait_visibility_of_element(PassRecoveryLocators.PASS_VISIBILITY)
        self.click_on_element(PassRecoveryLocators.PASS_VISIBILITY)

    @allure.step('Проверка отображения значения password')
    def check_visibility_of_pass_value(self):
        return self.check_element_visibility(PassRecoveryLocators.VALUE_PASSWORD_IS_VISIBLE)