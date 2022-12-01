# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('введите число '))



def decimaltobin(num):
    transfarr = []
    while num >= 2:
        transfarr.append(num%2)
        num = num // 2
    
    transfarr.append(1)

    decimal = ''
    for i in transfarr[::-1]:
        decimal = decimal + str(i)
    
    return int(decimal)

print(decimaltobin(num))