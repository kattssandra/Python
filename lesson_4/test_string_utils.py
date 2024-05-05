import pytest
from string_utils import StringUtils

@pytest.mark.positive_test_capitilize
@pytest.mark.parametrize('num, result', [('skypro, Skypro'), ('hello world, Hello world'), ('к, К')] )

def test_capitilize_positive(num, result):
    utils = StringUtils()
    res = utils.capitilize(num)  #skypro
    assert res == result
    print(res)

@pytest.mark.xfail
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('line, result', [("", ""),  # должен падать но проходит тест
# также должен падать но проходит
 (" ", " "), (None, None)])

def test_negative_capitilize(line, result):
    utils = StringUtils()
    res = utils.capitilize(line)
    assert res == result

def test_trim_positive():
    utils = StringUtils()
    res = utils.trim(" skypro")  # skypro
    assert res == "skypro"
    print(res)

def test_to_list_positive():
    utils = StringUtils()
    res = utils.to_list("1:2:3", ":")  #разделитель строк. По умолчанию запятая (",")
    assert res == ["1", "2", "3"]
    print(res)

def test_contains_positive():
    utils = StringUtils()
    res = utils.contains("SkyPro", "S")  #Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n
    assert res == True
    print(res)

def test_delete_symbol_positive():
    utils = StringUtils()
    res = utils.delete_symbol("SkyPro", "k")  #Удаляет все подстроки из переданной строки \n 
    assert res == "SyPro"
    print(res)

def test_starts_with_positive():
    utils = StringUtils()
    res = utils.starts_with("SkyPro", "S")  #Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n
    assert res == True
    print(res)

def test_end_with_positive():
    utils = StringUtils()
    res = utils.end_with("SkyPro", "o")   #Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
    assert res == True
    print(res)

def test_is_empty_positive():
    utils = StringUtils()
    res = utils.is_empty("")  # Возвращает `True`, если строка пустая и `False` - если нет \n
    assert res == True
    print(res)

def test_list_to_string_positive():
    utils = StringUtils()
    res = utils.list_to_string(["Sky", "Pro"], "-")  #Преобразует список элементов в строку с указанным разделителем \n 
    assert res == "Sky-Pro"
    print(res)