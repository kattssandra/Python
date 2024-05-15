from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text") #поиск элемента
element.send_keys("test skypro") #отправляем текст
element.clear() #очищаем текстовое поле
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click() #нажать на кнопку

 # Проверить корректность локатора (на сайте через консоль разработчика и команду $$).
 
print(element) #отображение результата в терминале

sleep(5)
driver.quit()