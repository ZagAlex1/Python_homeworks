# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4
import random

number_one = random.randint(1, 5)
number_two = random.randint(1, 5)

print(f'Первое число: {number_one}')
print(f'Второе число: {number_two}')


def sum_numbers(numb_1, numb_2):
    if numb_2 == 0:
        return numb_1
    return sum_numbers(numb_1 + 1, numb_2 - 1)


print(sum_numbers(number_one, number_two))

