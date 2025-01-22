from selenium.webdriver.common.by import By

class MainPageLocators:

    # Локатор кнопки Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Локатор кнопки Лента Заказов
    ORDER_FEED_BUTTON = (By.XPATH,  "//p[text()='Лента Заказов']")

    # Локатор кнопки Оформить Заказ
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Локатор заголовка Соберите бургер
    TITLE = (By.XPATH, "//h1")

    # Локатор ингредиента
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")

    # Локатор счетчика ингредиента
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    # Локатор корзины
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")

    # Локатор заголовка окна деталей ингредиента
    WINDOW_WITH_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Локатор кнопки закрытия попап
    ORDER_DETAILS_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button")

    # Локатор заголовка в окне оформленного заказа
    WINDOW_ORDER_TITLE = (By.XPATH, "//p[text()='идентификатор заказа']")

    # Локатор номера заказа
    ORDER_NUMBER_WINDOW = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")

    # Локатор закрытия окна
    WINDOW_ORDER_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")