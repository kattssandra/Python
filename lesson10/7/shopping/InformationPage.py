from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure

class Information:

    def __init__(self, browser):
        self.driver = browser

    # Заполните форму своими данными
    @allure.step("Ввод данных покупателя")
    def add_information(self, name: str, last_name: str, postal_code: str) -> None:
        self._driver.find_element(By.ID, 'first-name').send_keys(term)
        self._driver.find_element(By.ID, 'last-name').send_keys(term)
        self._driver.find_element(By.ID, 'postal-code').send_keys(term)
        sleep(10)

    # Нажмите кнопку Continue
    def button_continue(self):
        self._driver.find_element(By.ID, 'continue').click()