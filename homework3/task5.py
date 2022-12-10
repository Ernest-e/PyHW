# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

# def fibo (n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == -1:
#         return 1

#     fn = 1
#     fnm1 = 0


#     for i in range(2, n+1):
#         fn, fnm1 = fn+fnm1, fn

    
#     return fn


def negafibo(n):
    if n == 0:
        return 0

    res = [0 for _ in range(n*2+1)]
    res[n] = 0
    res[n+1] = 1
    res[n-1] = 1

    for i in range(n+2, len(res)):
        res[i] = res[i-1] + res[i-2]
    for i in range(n-2, -1, -1):
        res[i] = res[i+2] - res [i+1]

    return res

print(negafibo(8))

