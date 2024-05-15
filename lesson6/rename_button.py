from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейдите на сайт: http://uitestingplayground.com/textinput.
driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
field.clear()
field.send_keys("SkyPro")

# Нажмите на синюю кнопку
rename_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
rename_button.click()

# Получите текст кнопки и выведите в консоль (SkyPro).
text = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').text
print(text)

driver.quit()

