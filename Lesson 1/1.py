num = input(print('Введите трёхзначное число: '))

#  1 вариант
if len(num) != 3:
    print('Число не равно трём')
else:
    try:
        int(num)
        a = int(num[0])
        b = int(num[1])
        c = int(num[2])
        print(f'Сумма элементов числа составляет: {a+b+c}')
        print(f'Произведение элементов числа составляет: {a*b*c}')
    except ValueError:
        print('Вы ввели не число')

# 2 вариант
if len(num) != 3:
    print('Число не равно трём')
else:
    try:
        num = int(num)
        a = num % 10
        b = num // 10 % 10
        c = num // 100 % 10
        print(f'Сумма элементов числа составляет: {a+b+c}')
        print(f'Произведение элементов числа составляет: {a*b*c}')
    except ValueError:
        print('Вы ввели не число')