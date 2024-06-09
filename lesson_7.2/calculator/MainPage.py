from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage:

    # Откройте страницу:  https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        sleep(2)

    # В поле ввода по локатору #delay введите значение 45.

    def delay(self):
        self._driver.find_element(By.ID, 'delay').clear()
        self._driver.find_element(By.ID, 'delay').send_keys("45")

    # Нажми 7 + 8 =
    def click_buttons(self):
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[1]').click()
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[4]').click()
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[2]').click()
        self._driver.driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').click()
    
    #ожидание выполнения условий и результат:
    def wait_result(self):
        waiter = WebDriverWait(self.driver, 60) 
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15")) 
    
    def close_driver(self):
        self._driver.quit()