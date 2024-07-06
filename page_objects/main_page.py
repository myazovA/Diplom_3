from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_button_login(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_LOGIN)
        self.click_on_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Переход в Личный кабинет')
    def click_personal_account(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Переход к "Ленте заказов"')
    def click_orders_button(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_ORDERS)
        self.check_element_is_clickable(MainPageLocators.BUTTON_ORDERS)
        self.click_on_element(MainPageLocators.BUTTON_ORDERS)

    @allure.step('Переход к Конструктору')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Получение заголовка Конструктора')
    def get_constructor_title(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт"')
    def click_button_login(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_LOGIN)
        self.click_on_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.R2_D3_BUN)
        self.click_on_element(MainPageLocators.R2_D3_BUN)

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_ingredient_detail_title_visibility(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_DETAIL_TITLE)
        return self.check_element_visibility(MainPageLocators.INGREDIENT_DETAIL_TITLE)

    @allure.step('Проверка отсутствия окна "Детали ингредиента"')
    def check_ingredient_detail_closed(self):
        self.wait_for_closing_of_element(MainPageLocators.INGREDIENT_DETAIL_TITLE)
        if not self.check_element_visibility(MainPageLocators.INGREDIENT_DETAIL_TITLE):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_ingredient_detail(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CLOSE_INGREDIENT_DETAIL)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_INGREDIENT_DETAIL)

    @allure.step('Добавить интгридиент')
    def add_ingredient_to_basket(self):
        source_element = self.find_element_with_wait(MainPageLocators.R2_D3_BUN_PICTURE)
        target_element = self.find_element_with_wait(MainPageLocators.BASKET)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_ingredients_count(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_button_make_order(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_MAKE_ORDER)
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Окно подтверждения заказа отображается')
    def check_confirm_order_window_visibility(self):
        self.wait_visibility_of_element(MainPageLocators.CONFIRM_ORDER_WINDOW)
        return self.check_element_visibility(MainPageLocators.CONFIRM_ORDER_WINDOW)

    @allure.step('Получить номер в окне подтверждения заказа')
    def get_number_confirm_order(self):
        self.wait_for_element_to_change_text(MainPageLocators.NUMBER_CONFIRM_ORDER_WINDOW, '9999')
        return self.get_text_on_element(MainPageLocators.NUMBER_CONFIRM_ORDER_WINDOW)

    @allure.step('Закрыть окно подтверждения заказа')
    def click_button_close_confirm_order(self):
        self.check_element_is_clickable(MainPageLocators.BUTTON_CLOSE_CONFIRM_ORDER_WINDOW)
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CLOSE_CONFIRM_ORDER_WINDOW)
        self.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_CONFIRM_ORDER_WINDOW)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRM_ORDER_WINDOW)
