from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/") # Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/

for _ in range(5):  # Пять раз кликните на кнопку Add Element
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]') # Соберите со страницы список кнопок Delete

print("Размер списка: ", len(delete_buttons))  # Выведи размер списка кнопок "Delete"

sleep(5)
driver.quit()