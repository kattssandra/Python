import pytest
from calculator import Calculator

calculator=Calculator()

def test_sum_positive_nums():
    calculator=Calculator()
    res = calculator.sum(5,7) #++
    assert res == 12

def test_sum_negative_nums():
    calculator=Calculator()
    res = calculator.sum(-3,-5) #--
    assert res == -8

def test_sum_positive_and_negative_nums():
    calculator=Calculator()
    res = calculator.sum(-3,5) #--
    assert res == 2

def test_sum_float_nums():
    calculator=Calculator()
    res = calculator.sum(2.3, 4.3)  #..
    res=round(res, 1)
    assert res == 6.6

def test_sum_zero_nums():
    calculator=Calculator()
    res = calculator.sum(10,0) #n 0
    assert res == 10

def test_div_positive():
    calculator=Calculator()
    res = calculator.div(8, 4) 
    assert res == 2

def test_div_by_zero():
    calculator=Calculator()
    with pytest.raises(ArithmeticError):
      calculator.div(8, 0)  

def test_avg_empty_list():
    calculator=Calculator()
    nums=[]
    res = calculator.avg(nums)
    assert res == 0

def test_avg_positive():
    calculator=Calculator()
    nums=[22,4,8,6]
    res = calculator.avg(nums)
    assert res == 10
