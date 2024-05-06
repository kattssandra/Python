from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")  


for _ in range(5): # Пять раз кликните на кнопку Add Element
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]') # Соберите со страницы список кнопок Delete

# Выведи размер списка кнопок "Delete"
print("Размер списка: ", len(delete_buttons)) # Выведи размер списка кнопок "Delete"

driver.quit()