# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random


def input_number(msg):
    number = int(input(msg))
    return number


def new_list(size):
    number_list = [random.randint(1, 10) for _ in range(size)]
    return number_list


list_one = new_list(input_number('Введите размер первого списка: '))
list_two = new_list(input_number('Введите размер второго списка: '))

print(list_one)
print(list_two)

unique_list = []
for num_one in list_one:
    if num_one in list_two:
        unique_list.append(num_one)
print(sorted(set(unique_list)))

