from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Total:

    def __init__(self, browser):
        self.driver = browser

      # Проверьте, что итоговая сумма равна $58.29
    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        print(total)