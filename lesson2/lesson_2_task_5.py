def month_to_season(number):
       if number in [12, 1, 2]:
        return "Зима" 
       elif number in [3, 4, 5]:
        return "Весна"
       elif number in [6, 7, 8]:
        return "Лето"
       elif number in [9, 10, 11]:
        return "Осень"
       else:
        return "Введите цифры от 1 до 12"

number = int(input("Введите номер месяца (от 1 до 12): "))
season = month_to_season(number)
print(season)

