# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import copy


def removeall(args, num=''):
    while True:
        try:
            args.remove(num)
        except ValueError:
            break


mas1 = input('Введите элементы массива через пробел: ').split(' ')
removeall(mas1)
mas1 = [int(i) for i in mas1]
if len(mas1) <= 1:
    print('Слишком маленький массив')
else:
    mas2 = copy.deepcopy(mas1)
    mas2.remove(min(mas1))
    min1 = min(mas1)
    min2 = min(mas2)
    print('\nПервый способ:\n')
    print(f'Минимальное первое значение: {min1}\nМинимальное второе значение: {min2}')

# Второй способ
print('\nВторой способ:\n')
if len(mas1) <= 1:
    print('Слишком маленький массив')
else:
    mas2 = copy.deepcopy(mas1)
    mas2.sort()
    print(f'Минимальное первое значение: {mas2[0]}\nМинимальное второе значение: {mas2[1]}')
