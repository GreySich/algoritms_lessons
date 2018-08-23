a = input(print('Введите для уровнения y = a*x + b значение a: '))
b = input(print('Введите значение b: '))

try:
    int(a)
    int(b)
    print(f'Уравнение координат: y = {a}*x + {b}')
except ValueError:
    print('Вы ввели не числа')