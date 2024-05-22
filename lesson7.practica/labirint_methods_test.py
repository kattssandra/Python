from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

cookie = {"name": "cookie_policy", "value": "1"}
browser = None

def open_labirint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги по слову python (term)
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()    

def add_books():
    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter    

def go_to_cart():
     # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверяем счетчик книг. Должен быть равен числу нажатий
    txt = browser.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close_browser():
     browser.quit()

def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    open_labirint() # Открываем сайт
    search("Python") # Ищем книги по слову 
    # txt = browser.find_element( By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
    # assert txt == "Мы ничего не нашли по вашему запросу! Что делать?"
    added = add_books() # Добавляем книги и сохраняем результат в переменную 
    go_to_cart() # Идем в корзину 
    cart_counter = get_cart_counter() # Забираем значение счетчика из корзины
    assert added == cart_counter # Сравниваем counter со счетчиком корзины
    close_browser()


    
    