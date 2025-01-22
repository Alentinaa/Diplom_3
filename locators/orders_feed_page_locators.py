from selenium.webdriver.common.by import By

class OrdersFeedLocators:

    # Локатор кнопки Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # Локатор кнопки Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Локатор последнего заказа из Ленты заказов
    ORDER = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__2x95r')][1]")

    # Локатор номера последнего заказа из Ленты заказов
    ORDER_NUMBER_FROM_FEED = (
    By.XPATH, "//a[@class='OrderHistory_link__1iNby'][1]//p[contains(text(), 'Сегодня')]/preceding-sibling::p")

    # Локатор всплывающего окна с деталями заказа
    POPUP_ORDER_INFO = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")

    # Локатор счетчика выполнено за всё время
    COUNTER_ALL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    # Локатор счетчика Выполнено за сегодня
    COUNTER_TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Локатор поля с номером заказа из раздела В работе
    ORDER_IN_WORK = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")