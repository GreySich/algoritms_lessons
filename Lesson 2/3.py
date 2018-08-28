# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

num = list(input(print('Введите число: ')))

for i in range(len(num)):
    for j in range(len(num) - 1):
        if int(num[j]) < int(num[j+1]):
           vl = num[j+1]
           num[j+1] = num[j]
           num[j] = vl

print(f'Отсортированное число: {"".join(num)}')
