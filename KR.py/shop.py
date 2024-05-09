import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте сайт магазина: https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user
driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(10)

#Добавьте в корзину товары:

  #Sauce Labs Backpack
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
  # Sauce Labs Bolt T-Shirt
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
  # Sauce Labs Onesie
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click() 

# Перейдите в корзину
driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
sleep(10)

# Нажмите Checkout
driver.find_element(By.ID, 'checkout').click()

# Заполните форму своими данными
driver.find_element(By.ID, 'first-name').send_keys("Екатерина")
driver.find_element(By.ID, 'last-name').send_keys("Аверьянова")
driver.find_element(By.ID, 'postal-code').send_keys("247050")
sleep(10)

# Нажмите кнопку Continue
driver.find_element(By.ID, 'continue').click()

# Проверьте, что итоговая сумма равна $58.29
total = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
print(total)

sleep(5)

assert total == "$58.29" # падает здесь, не знаю как проверить

driver.quit()


