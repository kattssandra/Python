import math
def square(side):
    area = side **2
    if isinstance(area, int):
        return area 
    else:
        return math.ceil(area)
    


side = 2.6
print(square(side))
