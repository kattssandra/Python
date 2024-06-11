import allure
from MainPage import MainPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Калькулятор")
@allure.description("Проверка работы калькулятора")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_calculator():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Загрузка страницы калькулятора"):
        calculator = MainPage(driver)
    with allure.step("Выставление задержки выполнения действия"): 
        calculator.delay()
    with allure.step("Выполнени выражения"):  
        calculator.click_buttons()
    with allure.step("Сравненение значения выражения с числом 15"):
        assert calculator.result() == '15'
    with allure.step("Закрытие браузера Chrome"): 
        driver.quit()
    