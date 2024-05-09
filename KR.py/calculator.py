import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# В поле ввода по локатору #delay введите значение 45.
delay_rield = driver.find_element(By.ID, 'delay').clear()
delay_rield = driver.find_element(By.ID, 'delay').send_keys("45")


# Нажми 7 + 8 =
seven_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[1]').click()
plus_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[4]').click()
eigth_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[2]').click()
result_button = driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').click()

#ожидание выполнения условий:
waiter = WebDriverWait(driver, 45) 
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15")) #падает здесь, не понимаю почему
driver.implicitly_wait(45)

# Покажи результат
result = driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').text
print(result)

driver.quit()