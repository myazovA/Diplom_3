from page_objects.main_page import MainPage
from page_objects.orders_page import OrderPage
import allure


class TestMainPage:

    @allure.title('Переход в "Конструктор"')
    def test_go_to_constructor_success(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_button_constructor()
        assert 'Соберите бургер' in main_page.get_constructor_title()

    @allure.title('Переход в "Ленту заказов"')
    def test_go_to_orders_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_orders_button()
        assert order_page.get_orders_title() == 'Лента заказов'

    @allure.title('Открытие окна "Детали ингрелиента"')
    def test_click_on_igredient_details_open(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_ingredient()
        assert main_page.check_ingredient_detail_title_visibility()

    @allure.title('Закрытие окна "Детали ингредиента"')
    def test_close_ingredient_detail_window_closed(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_ingredient()
        main_page.close_ingredient_detail()
        assert main_page.check_ingredient_detail_closed()

    @allure.title('Добавление ингредиентов, увеличение показателя счетчика')
    def test_add_ingredients_counter_works(self, driver):
        main_page = MainPage(driver)

        main_page.add_ingredient_to_basket()
        assert main_page.get_ingredients_count() == '2'

    @allure.title('Оформление заказа пользователем')
    def test_user_make_order_order_created(self, driver, set_token):
        main_page = MainPage(driver)

        main_page.click_button_login()
        main_page.add_ingredient_to_basket()
        main_page.click_button_make_order()
        assert main_page.check_confirm_order_window_visibility()