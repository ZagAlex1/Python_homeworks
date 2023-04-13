# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

input_number = int(input('Введите число границу: '))

number = 1

while number < input_number:
    print(number, end=" ")
    number *= 2
