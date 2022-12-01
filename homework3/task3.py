# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


lst = [1.1, 1.2, 3.1, 5.0, 10.01]


# def diff (arr):
#     new_lst = []
#     for i in arr:
#         if isinstance(i, float) == True:
#             new_lst.append(float('0.'+str(i).split('.')[1]))
#         else:
#             new_lst.append(0.0)

#     return max(new_lst) - min(new_lst)



# print(diff(lst))

import random
from math import floor


arr = [1.1, 1.22313123, 3.1, 5.0, 10.01]
arr_dif = []
for i in arr:
    arr_dif.append(i - floor(i))
print(f'Разница между максимальным и минимальным значениями дробной части: {round(max(arr_dif)-min(arr_dif), 2)}, сгенирированный массив: {arr}')