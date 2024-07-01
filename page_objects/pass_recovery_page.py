from locators.pass_recovery_locators import PassRecoveryLocators
from page_objects.base_page import BasePage
from helpers import *
import allure

class PassRecoveryPage(BasePage):

    @allure.step('Проверка отображения поля email')
    def input_email_check(self):
        return self.check_element_visibility(PassRecoveryLocators.input_email)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PassRecoveryLocators.input_email)
        email = random_email()
        self.send_keys_to_input(PassRecoveryLocators.input_email, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PassRecoveryLocators.button_recover)
        self.click_on_element(PassRecoveryLocators.button_recover)

    @allure.step('Проверка отображения поля password')
    def check_input_password_visibility(self):
        self.wait_visibility_of_element(PassRecoveryLocators.input_password)
        return self.check_element_visibility(PassRecoveryLocators.input_password)

    @allure.step('Ввести пароль')
    def send_password(self):
        self.wait_visibility_of_element(PassRecoveryLocators.input_password)
        password = random_pass()
        self.send_keys_to_input(PassRecoveryLocators.input_password, password)

    @allure.step('Кликнуть на иноку видимости пароля')
    def click_pass_visibility_icon(self):
        self.wait_visibility_of_element(PassRecoveryLocators.pass_visibility)
        self.click_on_element(PassRecoveryLocators.pass_visibility)

    @allure.step('Проверка отображения значения password')
    def check_visibility_of_pass_value(self):
        return self.check_element_visibility(PassRecoveryLocators.value_password_is_visible)