from selenium.webdriver.common.by import By
from time import sleep

class MainPage:

    # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html.
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        sleep(2)
    
    def fields(self):
        # Заполните форму значениями:
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    
        # Нажмите кнопку Submit
        self._driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']").click()
    
    def get_zip_code(self):        
        zip_code = self._driver.find_element(By.CSS_SELECTOR, 'div[id="zip-code"]').value_of_css_property("color")
        return zip_code

    def get_all_fields(self):  
        all_fields = ["#first-name, #last-name, #address, #e-mail, #phone, #city, #country, #job-position, #company"]
        for field in all_fields:
            color = self._driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("color")
            return color
   