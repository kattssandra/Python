from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainShop import MainShop
from SwagLabs import SwagLabs
from YourCart import YourCart
from InformationPage import Information
from TotalPage import Total


def test_buying_process():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    MainShop = MainShop(browser)
    MainShop.authorize("standard_user", "secret_sauce")
    SwagLabs.add_labs()
    SwagLabs.cart()
    YourCart.checkout()
    Information.add_information("Екатерина", "Аверьянова", "123456")
    total = Total.total()
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29' but got '{total}'"
    
    browser.quit()

