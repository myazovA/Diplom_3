from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_button_login(self):
        self.wait_visibility_of_element(MainPageLocators.button_login)
        self.click_on_element(MainPageLocators.button_login)

    @allure.step('Переход в Личный кабинет')
    def click_personal_account(self):
        self.wait_visibility_of_element(MainPageLocators.button_personal_account)
        self.click_on_element(MainPageLocators.button_personal_account)

    @allure.step('Переход к "Ленте заказов"')
    def click_orders_button(self):
        self.wait_visibility_of_element(MainPageLocators.button_orders)
        self.click_on_element(MainPageLocators.button_orders)

    @allure.step('Переход к Конструктору')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.button_constructor)
        self.click_on_element(MainPageLocators.button_constructor)

    @allure.step('Получение заголовка Конструктора')
    def get_constructor_title(self):
        return self.get_text_on_element(MainPageLocators.constructor_title)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт"')
    def click_button_login(self):
        self.click_on_element(MainPageLocators.button_login)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.R2_D3_bun)
        self.click_on_element(MainPageLocators.R2_D3_bun)

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_ingredient_detail_title_visibility(self):
        self.wait_visibility_of_element(MainPageLocators.ingredient_detail_title)
        return self.check_element_visibility(MainPageLocators.ingredient_detail_title)

    @allure.step('Проверка отсутствия окна "Детали ингредиента"')
    def check_ingredient_detail_closed(self):
        self.wait_for_closing_of_element(MainPageLocators.ingredient_detail_title)
        if not self.check_element_visibility(MainPageLocators.ingredient_detail_title):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_ingredient_detail(self):
        self.wait_visibility_of_element(MainPageLocators.button_close_ingredient_detail)
        self.click_on_element(MainPageLocators.button_close_ingredient_detail)

    @allure.step('Добавить интгридиент')
    def add_ingredient_to_basket(self):
        source_element = self.find_element_with_wait(MainPageLocators.R2_D3_bun_picture)
        target_element = self.find_element_with_wait(MainPageLocators.basket)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_ingredients_count(self):
        return self.get_text_on_element(MainPageLocators.ingredient_counter)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_button_make_order(self):
        self.wait_visibility_of_element(MainPageLocators.button_make_order)
        self.click_on_element(MainPageLocators.button_make_order)

    @allure.step('Окно подтверждения заказа отображается')
    def check_confirm_order_window_visibility(self):
        self.wait_visibility_of_element(MainPageLocators.confirm_order_window)
        return self.check_element_visibility(MainPageLocators.confirm_order_window)

    @allure.step('Получить номер в окне подтверждения заказа')
    def get_number_confirm_order(self):
        self.wait_for_element_to_change_text(MainPageLocators.number_confirm_order_window, '9999')
        return self.get_text_on_element(MainPageLocators.number_confirm_order_window)

    @allure.step('Закрыть окно подтверждения заказа')
    def click_button_close_confirm_order(self):
        self.check_element_is_clickable(MainPageLocators.button_close_confirm_order_window)
        self.wait_visibility_of_element(MainPageLocators.button_close_confirm_order_window)
        self.find_element_with_wait(MainPageLocators.button_close_confirm_order_window)
        self.click_on_element(MainPageLocators.button_close_confirm_order_window)
