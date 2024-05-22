from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class YourCart:

    def __init__(self, browser):
        self.driver = browser

      # Нажмите Checkout
    def checkout (self):
        self._driver.find_element(By.ID, 'checkout').click()