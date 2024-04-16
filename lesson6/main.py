"""Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел -
элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)"""

# import random
# def list_creation(num):
#     list = []
#     for i in range(0, num):
#         list.append(random.randint(1, 10))
#     return list
# def comparison(list_1, list_2):
#     list = []
#     for num in list_1:
#         if num not in list_2:
#             list.append(num)
#     return list
# n = int(input("Введите количество элементов массива n: "))
# m = int(input("Введите количество элементов массива m: "))
# list_1 = list_creation(n)
# list_2 = list_creation(m)
# print(list_1)
# print(list_2)
# print(comparison(list_1, list_2))


# N = int(input())
# first_array = [int(input()) for _ in range(N)]
# M = int(input())
# second_array = {int(input()) for _ in range(M)} # Используем множество для быстрого поиска

# for num in first_array:
#     if num not in second_array:
#         print(num)

# def create_arr(st1):
#     return [int(input(f"Введите {i+1} элемент: ")) for i in range(int(input(st1)))]
# arr1 = create_arr("Число элементов массива 1: ")
# arr2 = create_arr("Число элементов массива 2: ")
# for el in arr1:
#     if el not in arr2:
#         print(el, end=" ")

# Определение функции create_arr, которая принимает строку st1 в качестве аргумента
# def create_arr(st1):
#  """Функция возвращает список чисел. Количество чисел и сами числа вводятся пользователем.
#  Функция input(st1) запрашивает у пользователя количество элементов.
#  Затем для каждого элемента от 0 до N-1 (где N - введенное пользователем число) выполняется цикл.
#  На каждой итерации цикла пользователь вводит число, которое добавляется в список."""
#     return [int(input(f"Введите {i+1} элемент: ")) for i in range(int(input(st1)))]

# # Создание первого списка чисел с помощью функции create_arr
# arr1 = create_arr("Число элементов массива 1: ")
# # Создание второго списка чисел с помощью функции create_arr
# arr2 = create_arr("Число элементов массива 2: ")

# # Перебор каждого элемента в первом списке
# for el in arr1:
# # Если текущий элемент не присутствует во втором списке,
# # то он выводится на экран (с пробелом в конце, но без перехода на новую строку)
#     if el not in arr2:
#         print(el, end=" ")

# nums = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     nums.append(n)

# nums = []
# for i in range(5):
#     nums.append(int(input("Введите число: ")))

# nums = [int(input("Введите число: ")) for i in range(5)]

# def creator_arr(length):
#     nums = [int(input("Введите число: ")) for i in range(length)]

# creator_arr(int(input("Введите длину: ")))

# print(*[f"{i}-й пошел" for i in range(1, 10)])

"""Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
(каждое число вводится с новой строки)"""

# import random
# def list_creation(num):
#     list = []
#     for i in range(0, num):
#         list.append(random.randint(1, 10))
#     return list
# def element_comparison(list_1):
#     counter = 0
#     i = 0
#     while i < len(list_1):
#         left_num = list_1[i - 1]
#         middle_num = list_1[i]
#         right_num = list_1[i - len(list_1) + 1]
#         i += 1
#         if left_num < middle_num > right_num:
#             counter += 1
#     return counter

# n = int(input("Введите количество элементов массива n: "))
# list_1 = list_creation(n)
# print(list_1)
# counter = element_comparison(list_1)
# print(counter)

# def create_arr(length):
#     return[random.randint(0, 99) for _ in range(length)]

# def count(arr):
#     counter = 0
#     for i in range(1, len(arr) -1):
#         if arr[i - 1] < arr[i] > arr[i + 1]:
#             counter += 1
#     return counter

# def recurs(arr):
#     if len(arr) <= 2:
#         return 0
#     counter = 0
#     if arr[1] > arr[0] and arr[1] > arr[2]:
#         counter += 1
#     return counter + recurs(arr[1:]) # каждый раз от списка отрезаем 2 элемента

# def recurs(arr):
#     if len(arr) <= 2:
#         return 0
#     counter = 0
#     if arr[1] > arr[0] and arr[1] > arr[2]:
#         counter += 1
#     return counter + recurs(arr[1:])

# arr = create_arr(16)
# print(arr)
# print("С помощью рекурсии:", recurs(arr))
# print("С помощью цикла:", count(arr))

""" Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. 
Все числа списка находятся на разных
строках.
Ввод: Вывод"""

# import random
# def list_creation(num):
#     list = []
#     for i in range(0, num):
#         list.append(random.randint(1, 10))
#     return list

# def element_comparison(list_1):
#     counter = 0
#     i = 0
#     for i in range(len(list_1)):
#         for j in range(i + 1, len(list_1)):
#             if list_1[i] == list_1[j]:
#                 counter += 1
#     return counter

# n = int(input("Введите количество элементов массива n: "))
# list_1 = list_creation(n)
# print(list_1)
# counter = element_comparison(list_1)
# print(counter)

# def count(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#     return count

# def recursive(numbers):
#     if len(numbers) <= 1:
#         return 0
#     first_num = numbers[0]
#     rest_nums = numbers[1:]
#     count = 0
#     for i in rest_nums:
#         if first_num == i:
#             count += 1
#     return count + recursive(rest_nums)

# arr = [1, 2, 3, 2, 2, 2, 2, 3, 3]
# print(recursive(arr))
# print(count(arr))
