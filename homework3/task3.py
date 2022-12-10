# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


lst = [1.1, 1.2, 3.1, 5.0, 10.01]


def diff (arr):
    new_lst = []
    for i in arr:
        if isinstance(i, float) == True:
            new_lst.append(float('0.'+str(i).split('.')[1]))
        else:
            new_lst.append(0.0)

    return max(new_lst) - min(new_lst)



print(diff(lst))

