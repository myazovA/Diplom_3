from page_objects.pass_recovery_page import PassRecoveryPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
import allure


class TestPassRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_pass_recovery_page_success(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        pass_rec_page = PassRecoveryPage(driver)

        main_page.click_button_login()
        login_page.go_to_pass_recovery()
        assert pass_rec_page.input_email_check()

    @allure.title('Переход к восстановлению пароля при вводе email и нажатии кнопки "Восстановить"')
    def test_click_recovery_button_with_email_success(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        pass_rec_page = PassRecoveryPage(driver)

        main_page.click_button_login()
        login_page.go_to_pass_recovery()
        pass_rec_page.send_email()
        pass_rec_page.click_on_recovery_button()
        assert pass_rec_page.check_input_password_visibility()


    @allure.title('Проверка отображения пароля в поле ввода после клика на иконку с глазом')
    def test_click_pass_visibility_icon_pass_is_visible(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        pass_rec_page = PassRecoveryPage(driver)

        main_page.click_button_login()
        login_page.go_to_pass_recovery()
        pass_rec_page.send_email()
        pass_rec_page.click_on_recovery_button()
        pass_rec_page.send_password()
        pass_rec_page.click_pass_visibility_icon()
        assert pass_rec_page.check_visibility_of_pass_value()