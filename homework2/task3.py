# Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму

n = int(input())
a = [(1+1/j)**j for j in range(1, n+1)]

for i in range (len(a)):
    print(a[i])

print()
print(sum(a))



