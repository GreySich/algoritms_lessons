# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_int(sm):
    if sm == 0:
        return 0
    else:
        return sm % 10 + sum_int(sm//10)


n = int(input(print('Введите количество чисел: ')))
mx = 0

for i in range(n):
    z = int(input(print(f'Введите {i + 1} число: ')))
    if sum_int(z) > sum_int(mx):
        mx = z

print(f'Число с максимальной суммой цифр: {mx}, а сама эта сумма: {sum_int(z)}')
