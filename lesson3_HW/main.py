""" Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1. Найдите количество и выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5, 3]
k = 3
# 1
# n = 0
# k = int(input("Введите число: "))
# list_1 = [1, 2, 3, 4, 5, 3, 3]
# for i in list_1:
#     if k == i:
#         n += 1
# print(n)

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)

print(nums.count(k))
"""

"""Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5

list_1 = [1, 2, 3, -4, -5]
k = 10
# num = list_1[0]
# for i in range(1, len(list_1)):
#     if abs(k - list_1[i]) <  abs(k - num):
#         num = list_1[i]
# print(num)

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)"""

""" В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Пример:
k = 'ноутбук'
# 12

dict_1 = {'AEIOULNSTRАВЕИНОРСТ' : 1, 'DGДКЛМПУ' : 2, 'BCMPБГЁЬЯ' : 3, 'FHVWYЙЫ' : 4, 'KЖЗХЦЧ' : 5, 'JXШЭЮ' : 8, 'QZФЩЪ' :10}
k = str(input("Введите слово: "))
cost = 0
for dictionary in dict_1: # Проходим по каждому словарю в списке
    for i in dictionary: # Продим по каждой букве в словаре
        for j in k:
            if i == j.upper():
                cost += dict_1.get(dictionary)
print(cost)"""

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)

# rus = {
#     "A":1,
#     "B":2
# }
# count = 0
# for letter in rus:
#     count += rus[letter]
# print(count)

# contacts = {"мама": 545234, "брат": 234653, "сестра": 234546}
# for i in contacts:
#     print(i)
    
# for key in contacts.keys():
#     print(key)
# print(contacts.keys())

# for numbers in contacts.values():
#     print(numbers)
    
# for cont, number in contacts.items():
#     print(number, cont)

dictionary_eng={"AEIOULNSTR":1, "DG":2, "BCMP":3, "FHVWY":4, "K":5, "JX":8, "QZ":10}

dictionary_rus={"АВЕИНОРСТ":1, "ДКЛМПУ" : 2, "БГЁЬЯ" : 3, "ЙЫ" : 4, "ЖЗХЦЧ":5, "ШЭЮ" : 8, "ФЩЪ":10 }

merged_dictionary = {**dictionary_eng, **dictionary_rus}

letters_dictionary=dict()
for key, value in merged_dictionary.items():
for letter in key:
letters_dictionary[letter]=value
dictionary_eng=dictionary_rus=merged_dictionary=None

k="ноутбук"
k=k.upper()