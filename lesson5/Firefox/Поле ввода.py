from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]') # Введи в поле 1000
input_field.send_keys("1000")
sleep(5)

input_field.clear() # Очисти это поле (метод clear)

input_field.send_keys("999") # Введи в это же поле  999

sleep(5)
driver.quit()