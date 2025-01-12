from selenium.webdriver.common.by import By

class AccountPageLocators:

    # Локатор кнопки История заказов
    ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")

    # Локатор кнопки Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Локатор кнопки Профиль
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")

    # Локатор номера заказа пользователя
    ORDER_NUMBER_FROM_HISTORY = (
    By.XPATH, "//a[@class='OrderHistory_link__1iNby']//p[contains(text(), 'Сегодня')]/preceding-sibling::p")