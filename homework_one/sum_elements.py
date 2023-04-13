# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

input_number = int(input('Введите число: '))
second_number = input_number // 10

sum_all_numbers = input_number // 100 + input_number % 10 + second_number % 10

print(sum_all_numbers)

