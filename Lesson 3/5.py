# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

mas = input('Введите элементы массива через пробел: ').split(' ')


def removeall(args, num=''):
    while True:
        try:
            args.remove(num)
        except ValueError:
            break


removeall(mas, '')
val = 0

# Первый способ
for i in mas:
    if int(i) < 0:
        if val == 0:
            val = i
        elif val > i:
            val = i

if val == 0:
    print('Такого элемента нет в массиве')
else:
    print(f'Максимальное минимальное {val} находится на {mas.index(val) + 1} позиции')

# Второй способ
mas2 = set(mas)
for i in set(mas):
    if int(i) >= 0:
        mas2.remove(i)

if len(mas2) == 0:
    print('Такого элемента нет в массиве')
else:
    print(f'Максимальное минимальное {max(mas2)} находится на {mas.index(max(mas2)) + 1} позиции')  # Правильно ли я понимаю, что в массиве отрицательных чисел максимальное -- это, по факту, минимальное?
    print(f'Максимальное минимальное {min(mas2)} находится на {mas.index(min(mas2)) + 1} позиции')  # В этом случае корректно получается
