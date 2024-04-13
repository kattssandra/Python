vklad = int(input('Скольков у вас денег? :'))
srok = int(input('Сколько лет будете хранить? :'))
stavka = 10/100
x = int(input(((vklad *stavka)*srok)+vklad))
print('Вы заберете сумму' , x)   
