# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input(print('Введите число: '))
evn = 0
odn = 0

for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        evn += 1
    else:
        odn += 1

print(f'У числа {num} {evn} чётных цифр и {odn} нечётных')
