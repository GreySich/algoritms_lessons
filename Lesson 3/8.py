# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

# Для ввода: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


def removeall(args, num=''):
    while True:
        try:
            args.remove(num)
        except ValueError:
            break


nums = input('Введите 15 чисел для мвссива через пробел').split(' ')
removeall(nums)
nums = [int(i) for i in nums]
column = []
mas = []
for i, n in enumerate(nums):
    column.append(n)
    if (i + 1) % 3 == 0:
        column.append(sum(column))
        mas.append(column)
        column = []

print('\nПолученная матрица: \n')
for i, _ in enumerate(mas):
    for j in mas[i]:
        print(j, end=' ')
    print('\n')
