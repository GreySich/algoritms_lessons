# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

str = string.ascii_uppercase
a = input(print('Номер буквы: '))
print(f'Весь алфавит: \n{str}')

try:
    a = int(a)
    if a > 26:
        print('В алфавите меньше символов')
    elif a < 1:
        print('Некорретно введено значение')
    else:
        print(f'Буква, которую вы искали -- это: {str[a-1]}')
except ValueError:
    print('Некорретно введено значение')
