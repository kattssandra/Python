from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Information:

    def __init__(self, browser):
        self.driver = browser

    # Заполните форму своими данными
    def add_information(self, term):
        self._driver.find_element(By.ID, 'first-name').send_keys(term)
        self._driver.find_element(By.ID, 'last-name').send_keys(term)
        self._driver.find_element(By.ID, 'postal-code').send_keys(term)
        sleep(10)

    # Нажмите кнопку Continue
    def button_continue(self):
        self._driver.find_element(By.ID, 'continue').click()