# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi

# def decimalplacespi(d):
#     precise = len(str(d))-2
#     return round(pi, precise)

# print(decimalplacespi(0.0001))

def decimalplacespi(d):
    precise = len(str(d))-2
    print(f'{pi:.{precise}f}')

decimalplacespi(0.001)