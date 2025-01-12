from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrderFeedPage
from data import OrderData
import allure
from urls import URLs


class TestBasicFunctionality:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Конструктор»')
    def test_click_construct_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_construct_button()
        assert main_page.get_current_url() == URLs.BASE_URL

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_click_order_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_current_url()
        assert main_page.get_current_url() == URLs.FEED

    @allure.title('Проверка основного функционала')
    @allure.description('Клик на ингредиент, открывает всплывающее окно с деталями')
    def test_click_ingredient_open_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_window_with_ingredient_detail_is_appear()

    @allure.title('Проверка основного функционала')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_by_click_x(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.click_window_with_detail_close_button()
        assert main_page.check_window_with_ingredient_detail_is_disappear()

    @allure.title('Проверка основного функционала')
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increasing_ingredient_counter(self, driver):
        order_data = OrderData.data_for_correct_order
        main_page = MainPage(driver)
        main_page.move_ingredient_to_order(order_data['ingredient'])
        assert main_page.check_ingredient_counter_is_increased()

    @allure.title('Проверка основного функционала')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_auth_user_can_create_order(self, driver):
        order_data = OrderData.data_for_correct_order
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page.wait_home_page_loading()
        main_page.move_ingredient_to_order(order_data['ingredient'])
        main_page.click_order_button()
        assert main_page.check_order_window_is_appear()

