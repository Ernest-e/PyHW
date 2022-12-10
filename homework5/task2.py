# 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)




def field (positions):
    print('Игровое поле:')
    print('--------------------------')
    for i in range(3):
        print('|', positions[i], '|', end='')

    print()
    print('--------------------------')
    for i in range(3,6):
        print('|', positions[i], '|', end='')
    print()
    print('--------------------------')
    for i in range(6,9):
        print('|', positions[i], '|', end='')
    print()
    print('--------------------------')

def player_move(mode:str, positions):
    check = True
    while check:
        print(f'На какую клетку поставить {mode}')
        pos = int(input())
        if positions[pos-1] != 'x' and positions[pos-1] != '0':
            positions[pos-1] = mode
            check = False
        else:
            print('Эта позиция занята')
    return positions

def win_situation(positions):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    x_pos = [i for i in range(9) if positions[i] == 'x']
    y_pos = [i for i in range(9) if positions[i] == '0']
    cont = True
    for i in win_positions:
        if x_pos == i:
            print("Победили крестики")
            cont = False
            break
        elif y_pos == i:
            print("Победили нолики")
            cont = False
            break
    return cont
        



def play (player1 = 'x', player2 ='0'):
    positions = [i for i in range(1,10)]
    go = True
    while go:
        field(positions=positions)
        print('Ход первого игрока')
        player_move(mode = player1, positions=positions)
        field(positions=positions)
        if win_situation(positions=positions) == False:
            go = False
            break
        print()
        print('Ход второго игрока')
        player_move(mode = player2, positions=positions)
        field(positions=positions)
        if win_situation(positions=positions) == False:
            go = False
            break

play()