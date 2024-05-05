from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# Найди кнопку "close" и кликни на нее
search_button = driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')
search_button.click()
sleep(5)

driver.quit()