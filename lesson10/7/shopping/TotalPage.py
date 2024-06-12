from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure

class Total:

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Текст общей стоимости записываем в переменную total")  
      # Проверьте, что итоговая сумма равна $58.29
    def total(self) -> str:
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        print(total)
        
    @allure.step("Закрытие браузера Chrome")
    def close(self)  -> None:
        self._driver.find_element(By.ID, "finish").click()
        self._driver.quit()