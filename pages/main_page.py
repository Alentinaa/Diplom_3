from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Ожидание полной загрузки главной страницы')
    def wait_home_page_loading(self):
        self.wait_element_loading(MainPageLocators.TITLE)

    @allure.step('Клик на кнопку Личный кабинет в правом верхнем углу главной страницы')
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(MainPageLocators.PROFILE_BUTTON)
        self.click_element(lk_button)

    @allure.step('Клик на кнопку Лента Заказов вверху главной страницы')
    def click_order_feed_button(self):
        order_feed_button = self.wait_and_find_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_element(order_feed_button)

    @allure.step('Клик на ингредиент в разделе Конструктор на главной странице')
    def click_ingredient(self):
        ingredient = self.wait_and_find_element(MainPageLocators.INGREDIENT)
        self.click_element(ingredient)

    @allure.step('Клик на кнопку закрытия всплывающего окна с деталями ингредиента')
    def click_window_with_detail_close_button(self):
        self.wait_and_find_element(MainPageLocators.ORDER_DETAILS_CLOSE_BUTTON).click()

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        order_button = self.wait_and_find_element(MainPageLocators.ORDER_BUTTON)
        self.click_element(order_button)

    @allure.step('Клик на кнопку закрытия окна оформленного заказа')
    def click_window_order_close_button(self):
        close_button = self.wait_and_find_element(MainPageLocators.WINDOW_ORDER_CLOSE_BUTTON)
        self.click_element(close_button)

    @allure.step('Перемещение ингредиента в корзину-конструктор')
    def move_ingredient_to_order(self):
        source_element = self.wait_and_find_element(MainPageLocators.INGREDIENT)
        target_element = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_BASKET)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Появление сплывающего окна с деталями ингредиента')
    def check_window_with_ingredient_detail_is_appear(self):
        title = self.wait_and_find_element(MainPageLocators.WINDOW_WITH_DETAILS_TITLE)
        return title.is_displayed()

    @allure.step('Закрытие всплывающего окна с деталями ингредиента')
    def check_window_with_ingredient_detail_is_disappear(self):
        title = self.wait_element_invisible(MainPageLocators.WINDOW_WITH_DETAILS_TITLE)
        return not title.is_displayed()

    @allure.step('Появление окна с деталями заказа')
    def check_order_window_is_appear(self):
        title = self.wait_and_find_element(MainPageLocators.WINDOW_ORDER_TITLE)
        num = self.wait_and_find_element(MainPageLocators.ORDER_NUMBER_WINDOW)
        return title.is_displayed() and num.text is not None

    @allure.step('Увеличение показателя счетчика ингредиента после добавления его в корзину-конструктор')
    def check_ingredient_counter_is_increased(self):
        counter = self.wait_and_find_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text) > 0