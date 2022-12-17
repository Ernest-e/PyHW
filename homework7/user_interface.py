import numpy as np

def mode():
    m = input('Выберите режим (1 -  создание нового контакта; 2 - поиск контакта)\n')
    return m

def what_to_add():
    print('СОЗДАНИЕ НОВОГО КОНТАКТА')
    data = []
    data.append(input('Введите фамилию: ').replace(' ', ''))
    data.append(input('Введите имя: ').replace(' ', ''))
    data.append(input('Введите отчество: ').replace(' ', ''))
    data.append(input('Введите номер: ').replace(' ', '').replace('(', '').replace(')', ''))
    data.append(input('Введите комментарий: '))
    return data
    
def search():
    print('ПОИСК КОНТАКТА')
    info = input('введите имя: ')
    return info

def show(info:list):
    if len(info) > 0:
        for i in info:
            print(i)
    else:
        print('Контакт не найден')



