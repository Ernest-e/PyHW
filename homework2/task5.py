# Реализуйте алгоритм перемешивания списка.

import random
lst = [1, 2, 3, 4, 5, 6, 7]

# for i in range(len(lst)-1, 0, -1):
#     j = random.randint(0, i+1)
#     temp = lst[i]
#     lst [i] = lst[j]
#     lst [j] = temp

# print(lst)


lst = random.shuffle(lst)
print(lst)