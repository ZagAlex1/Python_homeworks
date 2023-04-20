# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

size = int(input('Введите размер списка: '))
my_list = [random.randint(1, 20) for _ in range(size)]
print(my_list)
find_number = int(input('Введите число для проверки: '))

count = 0
min_dif = abs(my_list[0] - find_number)
nearest_number = my_list[0]
index = 0

for item in my_list:
    if find_number == item:
        count += 1
    else:
        while index < size:
            if min_dif > abs(my_list[index] - find_number):
                min_dif = abs(my_list[index] - find_number)
                nearest_number = my_list[index]
            index += 1
if count > 0:
    print(f'Число: {find_number} встретилось {count} раз (раза)')
else:
    print(f'Ближайшее число: {nearest_number}')

    dictionary
