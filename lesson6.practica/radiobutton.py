from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/radio-button")

is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
print(is_enabled)

is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
print(is_enabled)

driver.quit()

