# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# Для примера: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


def removeall(args, num=''):
    while True:
        try:
            args.remove(num)
        except ValueError:
            break


a = int(input('Введите количество столбцов для матрицы: '))
nums = input('Введите числа для мвссива через пробел').split(' ')
removeall(nums)
nums = [int(i) for i in nums]
column = []
mas = []
for i, n in enumerate(nums):
    column.append(n)
    if (i + 1) % a == 0:
        mas.append(column)
        column = []

if len(column) != 0:
    mas.append(column)

print('\nПолученная матрица: \n')
for i, _ in enumerate(mas):
    for j in mas[i]:
        print(j, end=' ')
    print('\n')

mins = []
for i in mas:
    mins.append(min(i))
print(f'наибольшее из наименьших {max(mins)}')