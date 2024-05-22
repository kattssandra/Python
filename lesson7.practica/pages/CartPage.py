from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def _init_ (self,browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.labirint.ru/cart/")

    def get_cart_counter(self):
        # Проверяем счетчик книг. Должен быть равен числу нажатий
        txt = self.driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
        return int(txt)