import allure
from MainPage import MainPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Поля ввода")
@allure.description("Тест проверяет, что фон незаполненного поля ввода при попытке перейти на следующую страницу красный")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_input_fields() -> None:
    with allure.step("Запуск браузера Chrome, переход на страницу с полями ввода"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        mainpaige_fields = MainPage(driver)

    with allure.step("Заполнение полей ввода"):
        mainpaige_fields.fields("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    
    with allure.step("Проверка: фон заполненных полей зеленый, незаполненного - красный"):
        assert mainpaige_fields.get_zip_code() == '#842029' # Проверьте (assert), что поле Zip code подсвечено красным.
    
    for color in mainpage_input_fields.get_other_fields_colors():
        assert mainpaige_fields.get_all_fields() == '#0f5132' # Проверьте (assert), что остальные поля подсвечены зеленым.
    
    with allure.step("Закрытие браузера Chrome"):
        driver.quit()


   