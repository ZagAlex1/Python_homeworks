# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

length_of_chocolates = int(input('Введите длину шоколадки: '))
chocolate_bar_width = int(input('Введите ширину шоколадки: '))
share_to_eat = int(input('Введите сколько хотите отломить долек: '))

number_of_chocolate_pieces = length_of_chocolates * chocolate_bar_width

if share_to_eat % chocolate_bar_width == 0 and share_to_eat < number_of_chocolate_pieces:
    print('Столько можно отломить')
else:
    print('Одним разломом не отделаться')
