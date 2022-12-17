import pandas as pd


class Database:
    def __init__(self):
        self.db = pd.DataFrame(columns=['Фамилия', 'Имя', 'Отчество', 'Номер', 'Комментарий'])

    def add(self, data:list):
        self.db.loc[len(self.db.index)+1] = data

    def find(self, name:str):
        res = []
        name = name.split()
        nums = self.db.query("Имя == @name[0] or Фамилия == @name[0] or Отчество == @name[0]").index
        if len(nums) == 0:
            print('Контакт не найден')
        else:
            for i in nums:
                res.append(tuple(self.db.loc[i]))
        if len(name)>1:
            for i in res:
                for j in range(len(name)):
                    if name[j] not in i:
                        res.remove(i)
        return res
    
    def log (self, file_name = 'contacts'):
        self.db.to_csv(file_name)
        with open (file_name+'.txt', 'a', encoding="utf-8") as fid:
            fid.write(self.db.to_string())
    
    def show_all(self):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.db)

