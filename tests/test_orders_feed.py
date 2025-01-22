import pytest
from data import OrderData
from locators.orders_feed_page_locators import OrdersFeedLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrderFeedPage
from pages.account_page import AccountPage
import allure

class TestOrdersFeed:

    @allure.title('Раздел «Лента заказов»')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_window_order_details_popup_opened(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_in_feed()
        assert order_feed_page.is_window_with_order_info_visible()

    @allure.title('Раздел «Лента заказов»')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_show_in_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page.wait_home_page_loading()
        main_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.wait_account_page_loading()
        account_page.click_orders_history_button()
        order_number = account_page.get_order_number_from_history()
        order_feed_page = OrderFeedPage(driver)
        last_order_number = order_feed_page.get_last_order_number_from_feed()
        assert last_order_number == order_number

    @allure.title('Раздел «Лента заказов»')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время/Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize('counter_locator', [
        OrdersFeedLocators.COUNTER_ALL_ORDERS,
        OrdersFeedLocators.COUNTER_TODAY_ORDERS
    ])

    def test_after_new_order_counter_increased(self, driver, counter_locator):
        order_data = OrderData.data_for_correct_order
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_counter_by_locator(counter_locator)
        order_feed_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page.wait_home_page_loading()
        main_page.move_ingredient_to_order(order_data['ingredient'])
        main_page.click_order_button()
        main_page.click_window_order_close_button()
        main_page.wait_home_page_loading()
        main_page.click_order_feed_button()
        new_count = order_feed_page.get_counter_by_locator(counter_locator)
        assert new_count > initial_count

    @allure.title('Раздел «Лента заказов»')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_user_order_displayed_in_order_in_work(self, driver):
        order_data = OrderData.data_for_correct_order
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_home_page_loading()
        main_page.move_ingredient_to_order(order_data['ingredient'])
        main_page.click_order_button()
        main_page.click_window_order_close_button()
        main_page.wait_home_page_loading()
        main_page.click_order_feed_button()
        order_number_from_ui = order_feed_page.get_number_of_order_in_work()
        order_data['order_number'] = order_number_from_ui
        assert order_number_from_ui == order_data['order_number']

