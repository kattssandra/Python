from pages.MainPage import MainPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fields():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    mainpaige_fields = MainPage(driver)
    mainpaige_fields.fields("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    
    assert mainpaige_fields.get_zip_code() == '#842029' # Проверьте (assert), что поле Zip code подсвечено красным.
    
    assert mainpaige_fields.get_all_fields() == '#0f5132' # Проверьте (assert), что остальные поля подсвечены зеленым.

    driver.quit()


   