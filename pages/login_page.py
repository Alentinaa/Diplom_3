from locators.login_page_locators import LoginPageLocators
from data import UserData
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step('Ввод email на странице авторизации')
    def input_email(self):
        self.wait_and_find_element(LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(UserData.data_correct['email'])

    @allure.step('Ввод пароля на странице авторизации')
    def input_password(self):
        self.wait_and_find_element(LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(UserData.data_correct['password'])

    @allure.step('Клик на кнопку Войти')
    def click_login_button(self):
        self.wait_and_find_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    @allure.step('Клик на ссылку Восстановить пароль')
    def click_recovery_password_link(self):
        self.wait_and_find_element(LoginPageLocators.RESET_PASSWORD_LINK).click()

