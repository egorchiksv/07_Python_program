""" Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
Пример
На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6 
3 6 9"""

# def print_operation_table(operation, num_rows = 9, num_cols = 9):
#     if num_rows > 2 and num_cols > 2:
#         for x in range(1, num_rows + 1):
#             for y in range(1, num_cols + 1):
#                 if num_cols == y:
#                     print(operation(x, y))
#                 else:
#                     print(operation(x, y), '', end='')
#     else:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')

# print_operation_table(lambda x, y: x*y, 3, 3)

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]))
    
# print_operation_table(lambda x, y: x*y, 3, 3)

"""Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.
Пример
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам пам-пам"""
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# def win_and_pooh(song):
#     volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
#     parts = song.split()
#     if len(parts) > 1:
#         itog = list()
#         for item in parts:
#             k = 0
#             for letter in item:
#                 if letter in volwes:
#                     k += 1
#             itog.append(k)
#         if len(set(itog)) == 1:
#             print('Парам пам-пам')
#         else:
#             print('Пам парам')
#     else:
#         print('Количество фраз должно быть больше одной!')

# win_and_pooh(stroka)

# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []
# for i in phrases:
#     countVowels.append(len([x for x in i if x.lower() in vowels]))
# if countVowels.count(countVowels[0]) == len(countVowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')