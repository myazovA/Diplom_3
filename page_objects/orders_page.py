from page_objects.base_page import BasePage
from locators.orders_page_locators import OrdersPageLocators
import allure


class OrderPage(BasePage):
    @allure.step('Получить текст заголовка раздела заказов')
    def get_orders_title(self):
        return self.get_text_on_element(OrdersPageLocators.orders_title)

    @allure.step('Кликнуть по заказу в ленте')
    def click_on_order_in_feed(self):
        self.wait_visibility_of_element(OrdersPageLocators.order_in_feed)
        self.click_on_element(OrdersPageLocators.order_in_feed)

    @allure.step('Получить текст заголовка окна с деталями заказа')
    def get_order_details_title(self):
        return self.get_text_on_element(OrdersPageLocators.order_details_title)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_all_orders_counter(self):
        self.find_element_with_wait(OrdersPageLocators.all_orders_counter)
        return self.get_text_on_element(OrdersPageLocators.all_orders_counter)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_daily_orders_counter(self):
        self.find_element_with_wait(OrdersPageLocators.daily_orders_counter)
        return self.get_text_on_element(OrdersPageLocators.daily_orders_counter)

    @allure.step('Проверить наличие номера заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = OrdersPageLocators.order_num_in_feed
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_element_visibility(locator_with_order_id)

    @allure.step('Получить номер последнего заказа в разделе "В работе"')
    def get_order_in_progress_num(self):
        self.wait_visibility_of_element(OrdersPageLocators.order_in_progress_num)
        return self.get_text_on_element(OrdersPageLocators.order_in_progress_num)