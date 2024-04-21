from calculator import Calculator

calculator=Calculator()


res = calculator.sum(5,7) #++
assert res == 12

res = calculator.sum(-3,-5) #--
assert res == -8

res = calculator.sum(-3, 5) #-+
assert res == 2

res = calculator.sum(2.3, 4.3) #..
res=round(res, 1)
assert res == 6.6

res = calculator.sum(10,0) #n 0
assert res == 10

#деление

res = calculator.div(8, 4)
assert res == 2

#среднее
nums=[]
res = calculator.avg(nums)
assert res == 0

nums=[22,4,8,6]
res = calculator.avg(nums)
assert res == 10

#деление на 0
res = calculator.div(8, 0)
assert res == None