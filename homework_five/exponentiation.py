# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number = int(input('Введите число: '))
extent = int(input('Введите степень: '))


def recursion_exp(numb, exp):
    if exp == 1:
        return numb
    elif exp == 0:
        return 1
    return numb * recursion_exp(numb, exp - 1)


print(recursion_exp(number, extent))
