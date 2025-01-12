from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    # Локатор поля ввода email
    RECOVERY_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")

    # Локатор поля ввода Пароля
    RESET_PASSWORD_FIELD = (By.XPATH, "//div[@class='input__icon input__icon-action']/parent::div")

    # Локатор кнопки Восстановить
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # показать/скрыть пароль
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")

