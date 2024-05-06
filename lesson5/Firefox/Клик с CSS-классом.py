from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

for _ in range(3):
    driver.get("http://uitestingplayground.com/classattr") # Откройте страницу http://uitestingplayground.com/classattr.
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    alert = driver.switch_to.alert
    alert.accept()

driver.quit()