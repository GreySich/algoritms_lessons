# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


while True:
    num1 = float(input(print('Введите первое число: ')))
    num2 = float(input(print('Введите второе число: ')))
    symb = input(print('Введите знак действия (при вводе 0, будет выход): '))
    while True:
        if symb not in ('0', '+', '-', '*', '/'):
            print('Некорректно введён знак действия. Повторите ввод:')
        else:
            break
    if symb == '0':
        break
    while True:
        if symb == '/' and num2 == 0:
            num2 = float(input(print('Нельзя делить на ноль \nПовторите ввод второго числа:')))
        else:
            break
    if symb == '+':
        print(f'Результат действия {num1} + {num2} == {num1 + num2}')
    elif symb == '-':
        print(f'Результат действия {num1} - {num2} == {num1 - num2}')
    elif symb == '*':
        print(f'Результат действия {num1} * {num2} == {num1 * num2}')
    else:
        print(f'Результат действия {num1} / {num2} == {num1 / num2}')
