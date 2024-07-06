from page_objects.orders_page import OrderPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.personal_account_page import PersonalAccountPage
import allure


class TestOrdersPage:

    @allure.title('Открытие окна Детали заказа')
    def test_open_order_details_opens(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_orders_button()
        order_page.click_on_order_in_feed()
        assert 'бургер' in order_page.get_order_details_title()

    @allure.title('Отображение только созданного заказа в ленте')
    def test_displaying_in_feed_new_order_from_history_success(self, driver, create_user_and_order_and_delete,
                                                               set_token):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        order_page = OrderPage(driver)

        main_page.click_personal_account()
        account_page.click_on_order_history_button()
        order_id = order_history_page.get_order_num()
        main_page.click_orders_button()
        assert order_page.check_id_order_in_feed(order_id)

    @allure.title('Увеличение общего количества заказов на счетчике')
    def test_add_order_all_order_counter_raise(self, driver, set_token):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_orders_button()
        orders_count_1 = order_page.get_all_orders_counter()
        main_page.click_on_button_constructor()
        main_page.click_button_login()
        main_page.add_ingredient_to_basket()
        main_page.click_button_make_order()
        main_page.get_number_confirm_order()
        main_page.click_button_close_confirm_order()
        main_page.click_orders_button()
        orders_count_2 = order_page.get_all_orders_counter()
        assert orders_count_1 < orders_count_2

    @allure.title('Увеличение ежедневного количества заказов на счетчике')
    def test_add_order_daily_order_counter_raise(self, driver, set_token):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_orders_button()
        orders_count_1 = order_page.get_daily_orders_counter()
        main_page.click_on_button_constructor()
        main_page.click_button_login()
        main_page.add_ingredient_to_basket()
        main_page.click_button_make_order()
        main_page.get_number_confirm_order()
        main_page.click_button_close_confirm_order()
        main_page.click_orders_button()
        orders_count_2 = order_page.get_daily_orders_counter()
        assert orders_count_1 < orders_count_2

    @allure.title('Новый заказ появляется в разделе "В работе"')
    def test_add_new_order_its_visible_in_work_section(self, driver, set_token):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_button_login()
        main_page.add_ingredient_to_basket()
        main_page.click_button_make_order()
        new_order_id = main_page.get_number_confirm_order()
        main_page.click_button_close_confirm_order()
        main_page.click_orders_button()
        assert order_page.get_order_in_progress_num() == '0'+new_order_id
