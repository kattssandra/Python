from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure

class SwagLabs:

    def _init_ (self,browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.saucedemo.com/")

    # Добавьте в корзину товары:
    @allure.step("Добавление товаров в корзину, запись общей стоимости в переменную")
    def add_labs(self) -> str:
        # Sauce Labs Backpack
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        # Sauce Labs Bolt T-Shirt
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        # Sauce Labs Onesie
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click() 
    
    # Перейдите в корзину
    @allure.step("Переход в корзину") 
    def cart(self)-> None:
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
        sleep(10)