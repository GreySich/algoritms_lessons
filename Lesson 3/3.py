# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import copy
n = int(input('Введите размер массива: '))
a = int(input('Введите диапазон для первого значения: '))
b = int(input('Введите диапазон для второго значения: '))


mas1 = []
mas1.append(random.randint(a, b))
for i in range(1, n):
    mas1.append(random.randint(a, b))

print('Исходный массив: ', end=' ')
for i in mas1:
    print(i, end=', ')

mas2 = copy.deepcopy(mas1)
mas3 = copy.copy(mas1)

# Делаем замены для двух видов массива (через deepcopy и через copy):
mas2[mas1.index(max(mas1))], mas2[mas1.index(min(mas1))] = min(mas1), max(mas1)
mas3[mas1.index(max(mas1))], mas3[mas1.index(min(mas1))] = min(mas1), max(mas1)


print('\nНовый массив через deepcopy: ', end=' ')
for i in mas2:
    print(i, end=', ')

print('\nНовый массив через copy: ', end=' ')
for i in mas3:
    print(i, end=', ')
