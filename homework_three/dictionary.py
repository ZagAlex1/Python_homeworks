# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, ёкоторое
# содержит либо только английские, либо только русские буквы.
# *Пример:*
#
# ноутбук
#     12

my_list_russian_one = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']  # 1 очко
my_list_russian_two = ['Д', 'К', 'Л', 'М', 'П', 'У']  # 2 очка
my_list_russian_three = ['Б', 'Г', 'Ё', 'Ь', 'Я']  # 3 очка
my_list_russian_four = ['Й', 'Ы']  # 4 очка
my_list_russian_five = ['Ж', 'З', 'Х', 'Ц', 'Ч']  # 5 очков

my_english_one = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']  # 1 очко
my_english_two = ['D', 'G']  # 2 очка
my_english_three = ['B', 'C', 'M', 'P']  # 3 очка
my_english_four = ['F', 'H', 'V', 'W', 'Y']  # 4 очка
my_english_five = ['K']  # 5 очков
my_english_eight = ['J', 'X']  # 8 очков
my_english_ten = ['Q', 'Z']  # 10 очков

my_dict_russian_list = [{1: my_list_russian_one}, {2: my_list_russian_two}, {3: my_list_russian_three},
                        {4: my_list_russian_four},
                        {5: my_list_russian_five}]
my_dict_english_list = [{1: my_english_one}, {2: my_english_two}, {3: my_english_three}, {4: my_english_four},
                        {5: my_english_five},
                        {8: my_english_eight}, {10: my_english_ten}]

