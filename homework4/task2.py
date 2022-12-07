# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def simplemults(n):
    res = []
    for i in range(1, n):
        if n % i == 0:
            if i not in res:
                res.append(i)
            n = n//i
        
    return res



print(simplemults(155))