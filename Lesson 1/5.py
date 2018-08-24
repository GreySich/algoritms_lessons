# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

a = input(print('Введите первый символ: ')).upper()
b = input(print('Введите второй символ: ')).upper()

str = string.ascii_uppercase

if len(a) != 1 or len(b) != 1 \
        or str.find(str) == -1 or str.find(b) == -1:
    print('Введены некорректные данные')
else:
    print(f'{a} находится на {str.find(a)+1} месте в алфавите')
    print(f'{b} находится на {str.find(b)+1} месте в алфавите')
    difs = abs(str.find(a) - str.find(b))
    if difs == 0:
        difs = 0
    else:
        difs -= 1
    print(f'Между {a} и {b} находится {difs} символа(ов)')
