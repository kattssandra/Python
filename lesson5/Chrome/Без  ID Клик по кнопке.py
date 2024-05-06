from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid") # Откройте страницу http://uitestingplayground.com/dynamicid

for _ in range(3): # Кликните на синюю кнопку. Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
    driver.get("http://uitestingplayground.com/dynamicid")
    button_with_dynamic_id = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button_with_dynamic_id.click()


sleep(5)
driver.quit()