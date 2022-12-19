import pandas as pd


class Database:
    def __init__(self):
        self.db = pd.DataFrame(columns=['id', 'Имя Фамилия', 'Номер телефона', 'Должность', 'email'])

    def add(self, data:list):
        if len(self.db.index) == 0:
            data[0] = str(1)
        else:
            data [0] = str(int(self.db['id'].iloc[-1]) + 1)
        self.db.loc[len(self.db.index)] = data

    def find(self, name:str):
        found = self.db.loc[self.db['Имя Фамилия'].str.contains(name, case = False)]
        if len(found) == 0:
            print('Сотрудник не найден')
        else:
            return found

    def delete(self, id):
        found = self.db.loc[self.db['id'].str.contains(id, case = False)]
        if len(found) == 0:
            print('Сотрудник не найден')
        else:
            self.db.drop(index = found.index, inplace = True)

    def edit(self, id, data):
        if data [0] in list(self.db['id']):
            print('Даннй id уже присвоен другому сотруднику')
        else:
            found = self.db.loc[self.db['id'].str.contains(id, case = False)]
            if len(found) == 0:
                print('Сотрудник не найден')
            else:
                self.db.iloc[found.index] = data

    def log (self, file_name = 'employees'):
        self.db.to_csv(file_name)
    
    def show_all(self):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.db)
