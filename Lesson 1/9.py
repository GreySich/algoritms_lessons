# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = input(print('Введите первое число: '))
b = input(print('Введите второе число: '))
c = input(print('Введите третье число: '))

try:
    a = float(a)
    b = float(b)
    c = float(c)
    if a != b and b != c and a != c:
        if a > b and a > c:
            if b > c:
                print(f'{b} -- среднее число')
            else:
                print(f'{c} -- среднее число')
        elif b > c and b > a:
            if a > c:
                print(f'{a} -- среднее число')
            else:
                print(f'{c} -- среднее число')
        else:
            if b > a:
                print(f'{b} -- среднее число')
            else:
                print(f'{a} -- среднее число')
    else:
        print('Не получится определить среднее, если есть равные числа')
except ValueError:
    print('Числа введены некорректно')
