def bank(X, Y):
    # Изначальная сумма на счету пользователя
    money = X

    for _ in range(Y):
        # Вычисляем сумму процентов за текущий год
        percent = money * 0.10
        # Добавляем проценты к сумме на счету
        money += percent

    return money

# Пример использования функции
X = float(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада в годах: "))
result = bank(X, Y)
print("Сумма на счету после", Y, "лет:", result)