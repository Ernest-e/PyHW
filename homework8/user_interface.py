def mode():
    m = input('Выберите режим (1 -  создание; 2 - поиск; 3 - редактирование; 4 - удаление; 5 - показать весь спискок )\n')
    return m

def what_to_add():
    print('СОЗДАНИЕ НОВОГО СОТРУДНИКА')
    data = [None]
    sec_name = (input('Введите фамилию: ').replace(' ', ''))
    name = (input('Введите имя: ').replace(' ', ''))
    person = sec_name + ' ' + name
    data.append(person)
    data.append(input('Введите номер телефона: ').replace(' ', '').replace('(', '').replace(')', ''))
    data.append(input('Введите должность: '))
    data.append(input('Введите email: '))
    return data

    
def search():
    print('ПОИСК СОТРУДНИКА')
    info = input('введите имя: ')
    return info


def what_to_edit():
    print('Изменение данных')
    info = input('введите id: ')
    return info

def edit_info():
    print('ИЗМЕНЕНИЕ ДАННЫХ')
    data = []
    data.append(input('Введите новый id: '))
    sec_name = (input('Введите фамилию: ').replace(' ', ''))
    name = (input('Введите имя: ').replace(' ', ''))
    person = sec_name + ' ' + name
    data.append(person)
    data.append(input('Введите номер телефона: ').replace(' ', '').replace('(', '').replace(')', ''))
    data.append(input('Введите должность: '))
    data.append(input('Введите комментарий: '))
    return data

def what_to_del():
    print('Удаление данных')
    info = input('введите id: ')
    return info

def show(info:list):
    if len(info) > 0:
        for i in info:
            print(i)
    else:
        print('Контакт не найден')
