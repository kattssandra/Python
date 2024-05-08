from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/visibility")
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed) #вывод статуса видимости Opacity 0

driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide # Opacity 0 окажется скрытой
sleep(2)

#еще раз проверим видимость Opacity 0:
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()

print(is_displayed) #еще раз выводим статус видимости Opacity 0

sleep(2)

driver.quit()

