# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


values = [0, 1]

for x in values:
    for y in values:
        for z in values:
            if not(x or y or z) == (not x and not y and not z):
                print (f'при значениях x = {x}, y = {y}, z = {z}, выражение истинно')
            else:
                print (f'при значениях x = {x}, y = {y}, z = {z}, выражение ложно')
