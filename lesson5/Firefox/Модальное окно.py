from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# Найди кнопку "close" и кликни на нее
search_button = driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')
search_button.click()
sleep(3)

driver.quit()