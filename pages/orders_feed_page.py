from pages.base_page import BasePage
import allure
from locators.orders_feed_page_locators import OrdersFeedLocators

class OrderFeedPage(BasePage):

    @allure.step('Клик на кнопку "Конструктор" в левом верхнем углу страницы Лента заказов')
    def click_construct_button(self):
        self.wait_and_find_element(OrdersFeedLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Клик на кнопку "Личный кабинет" в правом верхнем углу страницы Лента заказов')
    def click_lk_button(self):
        self.wait_and_find_element(OrdersFeedLocators.PROFILE_BUTTON).click()

    @allure.step('Клик на последний заказ в разделе Лента заказов')
    def click_order_in_feed(self):
        self.wait_and_find_element(OrdersFeedLocators.ORDER).click()

    @allure.step('Получение номера последнего заказа в разделе Лента заказов')
    def get_last_order_number_from_feed(self):
        order_num = self.wait_and_find_element(OrdersFeedLocators.ORDER_NUMBER_FROM_FEED)
        return int(order_num.text[2:])

    @allure.step('Получение значения счетчика Выполнено за всё время/Выполнено за сегодня')
    def get_counter_by_locator(self, locator):
        counter = self.wait_and_find_element(locator)
        return int(counter.text)

    @allure.step('Получение номера заказа из раздела В работе')
    def get_number_of_order_in_work(self):
        order_num = self.wait_and_find_element(OrdersFeedLocators.ORDER_IN_WORK)
        return int(order_num.text[1:])

    @allure.step('Проверка видимости всплывающего окна с деталями заказа')
    def is_window_with_order_info_visible(self):
        window = self.wait_and_find_element(OrdersFeedLocators.POPUP_ORDER_INFO)
        return window.is_displayed()

    @allure.step('Ожидание появления заказа в разделе В работе')
    def wait_order_in_work_to_appear(self):
        self.wait_element_loading(OrdersFeedLocators.ORDER_IN_WORK)
