from locators.forgot_password_page_locators import ForgotPasswordLocators
from data import UserData
from pages.base_page import BasePage
from urls import URLs
import allure

class ForgotPasswordPage(BasePage):

    @allure.step('Ввод email')
    def input_email(self):
        self.wait_and_find_element(ForgotPasswordLocators.RECOVERY_EMAIL_FIELD).send_keys(UserData.data_correct['email'])

    @allure.step('Клик на кнопку Восстановить')
    def click_recovery_button(self):
        self.wait_and_find_element(ForgotPasswordLocators.RECOVERY_BUTTON).click()

    @allure.step('Ожидание изменения url страницы"')
    def wait_redirect(self):
        return self.wait_url_change(URLs.FORGOT_PASSWORD)

    @allure.step('Клик на кнопку Показать/скрыть пароль в поле ввода пароля')
    def click_show_hide_password_button(self):
        self.wait_and_find_element(ForgotPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON).click()

    @allure.step('Клик на кнопку Показать/скрыть пароль делает поле активным')
    def reset_password_field_become_active(self):
        reset_password_field = self.wait_and_find_element(ForgotPasswordLocators.RESET_PASSWORD_FIELD)
        return 'input_status_active' in reset_password_field.get_attribute('class')