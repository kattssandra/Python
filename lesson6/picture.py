from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(40)

# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Получите значение атрибута src у 3-й картинки.
src = driver.find_element(By.CSS_SELECTOR, 'img[alt = "award"]').get_attribute("src")

#Выведите значение в консоль.
print(src)

driver.quit()