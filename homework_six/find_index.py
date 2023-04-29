# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

MIN_NUMBER = int(input('Введите минимальное значение диапазона: '))
MAX_NUMBER = int(input('Введите максимальное значение диапазона: '))

numbers_list = [random.randint(-5, 10) for _ in range(10)]
print(numbers_list)

index_list = []

for i in range(len(numbers_list)):
    if MIN_NUMBER < numbers_list[i] < MAX_NUMBER:
        index_list.append(i)

print(index_list)