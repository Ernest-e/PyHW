# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

sequence = [1, 22, 5235, 36, 364, 346, 364, 36, 22, 56, 5235]

def unique(lst):
    nonunique = []
    res = lst.copy()
    for i in range(len(sequence)):
        if sequence[i] in sequence[i+1:]:
            nonunique.append(sequence[i])

    for i in nonunique:
        count = nonunique.count(i)
        for j in range(count+1):
            res.remove(i)
            
    return res



print(unique(sequence))
