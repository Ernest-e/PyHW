# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

n = int(input())

lst = [i for i in range(-n, n+1)]
print(lst)

with open("file.txt", "r", encoding="utf-8") as fid:
    lines = fid.readlines()

product = 1
for line in lines:
        product *= lst[int(line.rstrip())]

print(product)