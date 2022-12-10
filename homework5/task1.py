# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

from numpy.random import randint

quantity = 117
max_grab = 28

def player_move (quantity = 117, max_grab = 28):
    grab = int(input(f'Сколько конфет взять? (максимум {max_grab}) '))
    chech_num = True
    while chech_num:
        if grab > 28:
            grab = int(input(f'Нельзя взять больше {max_grab}, сколько конфет взять? '))
        else:
            chech_num = False
    if grab > quantity:
        grab = quantity
    remains = quantity - grab
    if remains == 0:
        print('Поздравляем, вы победили')
        return remains
    else:
        return remains

def bot_move_stupid (quantity = 117, max_grab = 28):
    grab = randint(1,  max_grab)
    chech_num = True
    if grab > quantity:
        grab = quantity
    print(f'Бот взял {grab} конфет')
    remains = quantity - grab
    if remains == 0:
        print('Бот победил!')
        return remains
    else:
        return remains




def gamePvP(remains = 117):
    while remains != 0:
        print()
        print('Ход игрока №1')
        remains = player_move(quantity=remains, max_grab=max_grab)
        if remains == 0:
            break
        print('Остаток конфет = ', remains)
        print()
        print('Ход игрока №2')
        remains = player_move(quantity=remains, max_grab=max_grab)
        if remains == 0:
            break
        print('Остаток конфет = ', remains)



def gamePvB (remains = 117):
    while remains != 0:
        print()
        print('Ход игрока №1')
        remains = player_move(quantity=remains, max_grab=max_grab)
        if remains == 0:
            break
        print('Остаток конфет = ', remains)
        print()
        print('Ход бота')
        remains = bot_move_stupid(quantity=remains, max_grab=max_grab)
        if remains == 0:
            break
        print('Остаток конфет = ', remains)


gamePvP(remains=quantity)

# gamePvB(remains=quantity)

