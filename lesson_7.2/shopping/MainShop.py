from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainShop:

    # Откройте страницу:  https://www.saucedemo.com/
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        sleep(2)
    
    # Авторизуйтесь как пользователь standard_user
    def authorize(self, name, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        sleep(10)