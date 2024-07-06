from page_objects.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
import allure


class PersonalAccountPage(BasePage):
    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(PersonalAccountPageLocators.BUTTON_LOGOUT)

    @allure.step('Ожидание загрузки описания')
    def wait_description_visibility(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.PERS_ACC_DESCRIPTION)

    @allure.step('Проверка наличия описания')
    def check_description_visibility(self):
        return self.check_element_visibility(PersonalAccountPageLocators.PERS_ACC_DESCRIPTION)

    @allure.step('Ожидание загрузки кнопки "Зарегистрироваться"')
    def wait_button_register_visibility(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.BUTTON_REGISTER)

    @allure.step('Проверка наличия кнопки "Зарегистрироваться"')
    def check_button_register_visibility(self):
        return self.check_element_visibility(PersonalAccountPageLocators.BUTTON_REGISTER)