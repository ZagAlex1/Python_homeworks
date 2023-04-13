# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum_of_the_numbers = int(input('Введите сумму чисел: '))
multiply_of_the_numbers = int(input('Введите произведение чисел: '))

count = 1

while count < sum_of_the_numbers:
    if sum_of_the_numbers - count == multiply_of_the_numbers // count:
        print(f'Первое число = {count}; Второе число = {multiply_of_the_numbers // count}')
        break
    count += 1
