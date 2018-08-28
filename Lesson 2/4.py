# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input(print('Введите количество элементов: ')))
amn = 1
cnt = 1


def next_element(val, i):
    if i == n:
        return f'{i}, {val}'
    else:
        return next_element(-val/2, i+1)


print(next_element(amn, cnt))
