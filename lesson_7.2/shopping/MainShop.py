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
    def authorize(self):
        self._driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        self._driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()
        sleep(10)