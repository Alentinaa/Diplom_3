from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
import allure
from urls import URLs


class TestForgotPassword:

    @allure.title('Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_forgot_password_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        current_url = driver.get_current_url()
        assert current_url == URLs.FORGOT_PASSWORD

    @allure.title('Восстановление пароля')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_set_email_and_reset_password(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_email()
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_redirect()
        current_url = driver.get_current_url()
        assert current_url == URLs.RESET_PASSWORD

    @allure.title('Восстановление пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_show_password_button_highlighted_field(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_email()
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_redirect()
        forgot_password_page.click_show_hide_password_button()
        is_active = forgot_password_page.reset_password_field_become_active()
        assert is_active

