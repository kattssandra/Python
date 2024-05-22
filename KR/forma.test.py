from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(4)
def test_input_fields():
    # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html.
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html") 
    # Заполните форму значениями:
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    sleep(5)
    # Нажмите кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']").click()
    sleep(10)

    # Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code = driver.find_element(By.CSS_SELECTOR, 'div[id="zip-code"]').value_of_css_property("color")
    assert zip_code == ("#842029") 
    
    # Проверьте (assert), что остальные поля подсвечены зеленым.
    all_fields = ["#first-name, #last-name, #address, #e-mail, #phone, #city, #country, #job-position, #company"]
    for field in all_fields:
        color = driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("color")
    assert color == ("#0f5132")

driver.quit()

 
