""" Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()"""

# string = input("Введите строку:").split()
# result = dict()
# for i in string:
#     if i in result.keys():
#         print(f'{i}_{result[i]}', end = " ")
#         result[i] += 1
#     else:
#         print(i, end = " ")
#         result[i] = 1


# list_1 = 'a a a b c a a d c d d'
# input_list = list_1.split()

# a = ''
# dict_1 = {}
# for i in input_list:
#     a += i
#     if i in dict_1:
#         dict_1[i] += 1
#         a += f'_{dict_1[i]}'
#     else:
#         dict_1[i] = 0
#         a += ' '

# print(a)

# string = input("Введите строку:").split()
# result = dict()
# new_result = ""
# for i in string:
#     if i in result.keys():
#         new_result += f"{i}_{result[i]}"
#         result[i] += 1
#     else:
#         new_result += i
#         result[i] = 1
#     new_result += " "
# print(new_result)

# string = input("Введите строку:").split()
# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
# print(" ".join(new_result))

# string = input("Введите строку:").split()
# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
# print(*new_result)

# text = "a a a b c a a d c d d"
# new_text = ""
# for letter in text.split(" "):
#     counter = 0
#     for find_letters in new_text:
#         if find_letters == letter:
#             counter +=1
#     if counter > 0:
#         new_text += letter + "_" + str(counter) + " "
#     else:
#         new_text += letter + " "
# print(new_text)

""" Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells.
Output: 13"""

# string = '''She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells'''
# print(len(set(string.lower().split())))
# string_new = string.lower().split()
# string_new = set(string_new)
# print(len(string_new))

# sym = ".,!?:;"
# str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# str = str.lower()
# for s in sym:
#     str = str.replace(s, " ")
# res = set(str.split())
# print(len(res))

""" Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих слайдах"""

# High = 0
# number = None
# while number != 0:
#     number = int(input("Введите число: "))
#     if number > High:
#         High = number
# print(High)

# n = None
# b = set()
# while n != 0:
#     n = int(input("Введите число: "))
#     if n > 0:
#         b.add(n)
#     else:
#         continue
# max_num = max(b)
# print(max_num)

# a = [7, 5, 8, 124, 234, 1, 3, 66 , 0 ,144 , 1 , 0]
# a_max = 0
# for i in range (len(a)):
#     if a[i] > a_max:
#         a_max = a[i]
# print(a_max)

# a = [7, 5, 8, 124, 234, 1, 3, 66 , 0 ,144 , 1 , 0]
# print(max(a))