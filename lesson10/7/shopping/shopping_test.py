from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainShop import MainShop
from SwagLabs import SwagLabs
from YourCart import YourCart
from InformationPage import Information
from TotalPage import Total
import allure

@allure.title("Проверка итоговой стоимости в интернет-магазине")
@allure.description("Тест сравнивает сумму добавленных в корзину товаров с конкретным значением")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_buying_process():
    with allure.step("Запуск браузера Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    with allure.step("Переход на страницу интернет-магазина"):
        MainShop = MainShop(browser)

    with allure.step("Авторизация"):
        MainShop.authorize("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
        SwagLabs.add_labs()

    with allure.step("Переход в корзину"):
        SwagLabs.cart()

    with allure.step("Ввод данных покупателя"):
        YourCart.checkout()
        Information.add_information("Екатерина", "Аверьянова", "123456")
    
    with allure.step("Сравнение итоговой стоимости с конкретным значением"):
        total = Total.total()
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29' but got '{total}'"
    

    with allure.step("Закрытие браузера Chrome"): 
        browser.quit()

