# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [2, 3, 4, 5, 6]


def mult(lst):
    res = []
    for i in range(len(lst)//2):
        res.append(lst[i]*lst[-1*(i + 1)])

    if len(lst)%2 != 0:
        res.append(lst[(len(lst)//2)]**2)

    return res


print(mult(lst))