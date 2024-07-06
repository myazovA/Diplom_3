from page_objects.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Data
import allure


class LoginPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def go_to_pass_recovery(self):
        self.wait_visibility_of_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD)
        self.click_on_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD)



