from string_utils import StringUtils

utils = StringUtils()

res = utils.capitilize("skypro")  #skypro
assert res == "Skypro"
print(res)

res = utils.trim(" skypro")  #skypro без пробела
assert res == "skypro"
print(res)

res = utils.to_list("1:2:3", ":")  #разделитель строк. По умолчанию запятая (",")
assert res == ["1", "2", "3"]
print(res)

res = utils.contains("SkyPro", "S")  #Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
assert res == True
print(res)

res = utils.delete_symbol("SkyPro", "k")  #Удаляет все подстроки из переданной строки \n 
assert res == "SyPro"
print(res)

res = utils.starts_with("SkyPro", "S")  #Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n
assert res == True
print(res)

res = utils.end_with("SkyPro", "o")  #Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
assert res == True
print(res)

res = utils.is_empty("")  #Возвращает `True`, если строка пустая и `False` - если нет \n 
assert res == True
print(res)

res = utils.list_to_string(["Sky", "Pro"], "-")  #Преобразует список элементов в строку с указанным разделителем \n 
assert res == "Sky-Pro"
print(res)