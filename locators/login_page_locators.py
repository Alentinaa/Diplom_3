from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Локатор поля ввода email
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")

    # Локатор поля ввода пароля
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

    # Локатор кнопки Войти
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//Button[text()='Войти']")

    # Локатор ссылки Восстановить пароль
    RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")