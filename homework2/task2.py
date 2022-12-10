# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

import math
n = int(input())
res = []
for i in range(1, n+1):
    res.append(math.factorial(i))
    
print(res)

