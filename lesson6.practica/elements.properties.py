from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

sleep(20)

txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text
#в переменную с методом text соберется информация об элементе

tag = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name
id = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').id
ff = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("font-family")
print(ff)
color = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("color") #цвет
print(color)
height = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("height") #размер
print(height)
letter_spacing = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("letter-spacing")
print(letter_spacing)

print(tag)
print(txt) #запрос выведет информацию из переменной в терминал
print(id)

driver.quit() #закрываем драйвер