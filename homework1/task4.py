#  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

x = int(input('Введите номер четверти: '))

if x > 0 and x <=4:
    if x == 1:
        print('x Э (0; +inf), y Э (0; + inf)')
    elif x == 2:
        print('x Э (0; -inf), y Э (0; +inf)')
    elif x == 3:
        print('x Э (0; -inf), y Э (0; -inf)')
    elif x == 4:
        print('x Э (0; +inf), y Э (0; -inf)')
else:
    print("Error")

