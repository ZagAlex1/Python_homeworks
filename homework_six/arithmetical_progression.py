# Задача 30: Заполните список элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый элемент: '))
diff = int(input('Введите разность: '))
size = int(input('Введите количество элементов: '))

progression_list = []
progression_list.insert(0, first_element)

for i in range(size - 1):
    progression_list.append(progression_list[i] + diff)

print(progression_list)
