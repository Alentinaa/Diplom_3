from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from urls import URLs
import allure


class AccountPage(BasePage):

    @allure.step('Ожидание загрузки страницы Личный Кабинет')
    def wait_account_page_loading(self):
        self.wait_element_loading(AccountPageLocators.PROFILE_BUTTON)

    @allure.step('Нажать на кнопку История заказов')
    def click_orders_history_button(self):
        orders_history_link = self.wait_and_find_element(AccountPageLocators.ORDERS_HISTORY)
        orders_history_link.click()

    @allure.step('Нажать на кнопку Выход')
    def click_logout_button(self):
        logout_button = self.wait_and_find_element(AccountPageLocators.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", logout_button)

    @allure.step('Получить номер заказа пользователя из раздела История заказов')
    def get_order_number_from_history(self):
        order_num = self.wait_and_find_element(AccountPageLocators.ORDER_NUMBER_FROM_HISTORY)
        return int(order_num.text[2:])

    @allure.step('Ожидание, когда url страницы изменится')
    def wait_redirect(self):
        return self.wait_url_change(URLs.ACCOUNT)

