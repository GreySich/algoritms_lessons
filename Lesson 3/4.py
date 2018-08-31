# 4. Определить, какое число в массиве встречается чаще всего.

# С этой задачи изменил методы ввода массива на более удобный
mas = input('Введите числа через пробел').split(' ')

cnt, num = 0, ''
# В моих проверках слишком часто ставил лишние пробелы
while True:
    try:
        mas.remove(num)
    except ValueError:
        break

for i in set(mas):
    if mas.count(i) > cnt:
        cnt, num = mas.count(i), i
print(f'{num} встречается чаще всего: {cnt} раз(а)')
