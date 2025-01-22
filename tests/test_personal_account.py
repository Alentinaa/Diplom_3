import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from urls import URLs


class TestPersonalAccount:

    @allure.title('Личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_click_account_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        current_url = login_page.get_current_url()
        assert current_url == URLs.LOGIN

    @allure.title('Личный кабинет')
    @allure.description('Переход в раздел «История заказов»')
    def test_click_to_orders_history_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page.wait_home_page_loading()
        main_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.click_orders_history_button()
        current_url = main_page.get_current_url()
        assert current_url == URLs.ORDER_HISTORY

    @allure.title('Личный кабинет')
    @allure.description('Выход из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page.wait_home_page_loading()
        main_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        account_page.wait_redirect()
        current_url = main_page.get_current_url()
        assert current_url == URLs.LOGIN

