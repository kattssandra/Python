from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(40)

# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# дождаться загрузки всех картинок
wait = WebDriverWait(driver, 10, 0.1)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(4)")))

# Получите значение атрибута src у 3-й картинки.
src = driver.find_element(By.CSS_SELECTOR, 'img[alt = "award"]').get_attribute("src")

# Выведите значение в консоль.
print(src)

driver.quit()