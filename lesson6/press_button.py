from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Перейдите на страницу http://uitestingplayground.com/ajax.
driver.get("http://uitestingplayground.com/ajax") 

#Нажмите на синюю кнопку
blue_button = driver.find_element(By.ID,'ajaxButton')
blue_button.click()
driver.implicitly_wait(40)


#Получите текст из зеленой плашки.
txt = driver.find_element(By.CSS_SELECTOR,'p[class="bg-success"]').text

#Выведите его в консоль (Data loaded with AJAX get request).
print(txt) 
driver.quit()