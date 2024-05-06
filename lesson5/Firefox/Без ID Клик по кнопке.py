from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid") # Откройте страницу http://uitestingplayground.com/dynamicid

for _ in range(3): # Кликните на синюю кнопку. Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
    driver.get("http://uitestingplayground.com/dynamicid")
    button_with_dynamic_id = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button_with_dynamic_id.click()


driver.quit()