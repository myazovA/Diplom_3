from locators.order_history_page_locators import OrderHistoryPageLocators
from page_objects.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step('Ожидание карточки заказа')
    def wait_order_card_visibility(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_CARD)

    @allure.step('Получить заголовок заказа')
    def get_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_TITLE)

    @allure.step('Получить номер заказа')
    def get_order_num(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_NUM)