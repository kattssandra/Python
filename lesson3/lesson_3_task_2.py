from smartphone import Smartphone

phone1 = Smartphone("Айфон", "125",375291225698)
phone2 = Smartphone("Самсунг", "Гелекси", 375294445698)
phone3 = Smartphone("Ксяоми", "Промакс", 375191225697)
phone4 = Smartphone("Нокиа", "777", 375291227798)
phone5 = Smartphone("Поко", "м5", 375291226998)


catalog = [phone1, phone2, phone3, phone4, phone5]
for i in catalog:
    i.sayphone()