from page_objects.personal_account_page import PersonalAccountPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
import allure


class TestPersonalAccountPage:
    @allure.title('Переход в "Личный кабинет"')
    def test_go_to_account_page_success(self, driver, set_token):
        main_page = MainPage(driver)
        pers_account_page = PersonalAccountPage(driver)

        main_page.click_personal_account()
        pers_account_page.wait_description_visibility()
        assert pers_account_page.check_description_visibility()

    @allure.title('Переход к «Истории заказов»')
    def test_go_to_order_history_page_success(self, driver, set_token, create_user_and_order_and_delete):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)

        main_page.click_personal_account()
        account_page.wait_description_visibility()
        account_page.click_on_order_history_button()
        order_history_page.wait_order_card_visibility()
        assert 'бургер' in order_history_page.get_order_card_title()

    @allure.title('Выход из аккаунта кнопкой "Выйти"')
    def test_pers_acc_exit_logout(self, driver, set_token):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)

        main_page.click_personal_account()
        account_page.wait_description_visibility()
        account_page.click_on_logout_button()
        account_page.wait_button_register_visibility()
        assert account_page.check_button_register_visibility()