# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


def removeall(args, num=''):
    while True:
        try:
            args.remove(num)
        except ValueError:
            break


mas = input('Введите элементы массива через пробел: ').split(' ')
removeall(mas)
# print(mas)
mas = [float(i) for i in mas]
# print(mas)
sm = 0

for i in range(mas.index(min(mas))+1, mas.index(max(mas))):
    sm += mas[i]

print(f'Сумма элементов: {sm}')
