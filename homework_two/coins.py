# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

number_of_coins = int(input('Введите общее количество монеток: '))
eagle = 0
tails = 0
index = 0

while index < number_of_coins:
    side_of_the_coin = random.randint(0, 1)
    if side_of_the_coin == 0:
        eagle += 1
    else:
        tails += 1
    index += 1

print(f'Лежат орлом: {eagle}')
print(f'Лежат решкой: {tails}')

if eagle > tails:
    print(f'Минимально нужно перевернуть: {tails} шт.')
else:
    print(f'Минимально нужно перевернуть: {eagle} шт.')


