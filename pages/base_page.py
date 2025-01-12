import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузка элемента с явным ожиданием')
    def wait_element_loading(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Поиск элемента с ожиданием')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_element(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Перетащить и отпустить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        return drag_and_drop(self.driver, source_element, target_element)

    @allure.step('Ожидание изменения урла')
    def wait_url_change(self, old_url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(old_url))

    @allure.step('Получить текущий урл')
    def get_current_url(self):
        return self.driver.current_url