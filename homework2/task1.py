# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# a = input().split(',')
# sum = 0
# if len(a)>1:
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             sum += int(a[i][j])
# else:
#     for i in range(len(a[0])):
#         sum += int(a[0][i])


# print (sum)


a = input().replace(',', '')
sum = 0
for i in range(len(a)):
    sum += int(a[i])


print (sum)




# print({n: 3*n+1 for n in range(5)})

# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# a = [(-3)**n for n in range(5)]
# print(a)
# 2. {n: 3*n+1 for n in range(n)}
# 3. a = input()
# b = input()
# print(a.count(b))


# a = input()
# b = input()
# print(a.count(b))


# for i in range(5):
#     # print(i)
#     print((-3)**i)




# 2'. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# n = int(input())
# dict = {}
# for i in range(1, n):
#     res = 3*i + 1
#     dict[i] = res

# print(dict)


# print({n: 3*n+1 for n in range(1, 6)})



3. #  Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# a = input()
# b = input()
# if len(a)>len(b):
#     print(a.count(b))
# else:
#     print(b.count(a))

