from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
browser.maximize_window() #для разворачивания окна
browser.get("https://ya.ru/") #для перехода на нужную страницу
browser.save_screenshot("./ya2.png") #для сохранения скриншота
browser.quit() #для закрытия окна
