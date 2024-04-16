# import time
# import sys
# sys.setrecursionlimit(5000) # Стандартно рекурсия может повторяться 996 раз, если нужно больше, то используем sys.setrecursionlimit()
# def factorial(end):
# #    time.sleep(0.1)
#     if end == 1: # если переполнился стек, нужно сделать return
#         return 1
#     return factorial(end - 1) * end
# summa = factorial(5)
# print(summa)

# rub = 1
# for i in range(996):
#     print(rub)
#     time.sleep(0.1)
#     rub += 1
    
"""Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где
a0  = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
Числа Фибоначчи 0 1 1 2 3 5 8 13 21"""

# def fibonacci(N):
#     if N <= 1:
#         return N
#     return fibonacci(N - 1) + fibonacci(N - 2)

# for i in range(3):
#     print(fibonacci(i), end=" " )   
    
# print(fibonacci(3))

"""Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1"""

# def revers(grades):
#     min_grade = min(grades)
#     max_grade = max(grades)
#     list1 = []
#     for grade in grades:
#         if grade == max_grade:
#             list1.append(min_grade)
#         else:
#             list1.append(grade)
#     return list1

# grades = [1,5,4,5,3]
# result = revers(grades)
# print(result)

# import random
# list_1 = list()
# for i in range (0, 5):
#     number = random.randint(1, 5)
#     list_1.append(number)
# print(list_1)
# min_num = min(list_1)
# max_num = max(list_1)
# for j in range(len(list_1)):
#     if list_1[j] == max_num:
#         list_1[j] = min_num

# print(list_1)

# def max_on_min(arr):
#     max_val = max(arr)
#     min_val = min(arr)
#     for i in range(len(arr)):
#         if arr[i] == max_val:
#             arr[i] = min_val
#     pass

# arr = [1, 3, 3, 3, 4]
# max_on_min(arr)
# print(arr)

"""Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes"""

# def is_prime(N):
#     if N % 2 == 0:
#         return 'no'
#     for i in range(3, N // 2, 2):
#         if N % i == 0:
#             return 'no'
#     return 'yes'
# print(is_prime(6))

# def func(n):
#     num = 2
#     while n % num != 0:
#         num += 1
#     return num == n
# print(func(6))

# def simple_number(number, dev = 2):
#     if number==dev:
#         #print('yes')
#         return 'yes'
#     if number%dev==0:
#         #print('no')
#         return 'no'
#     return simple_number(number, dev+1)
# print(simple_number(15))

""" Задача №37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в
обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 
Output: 4 3"""

# def revers_values(N):
#     num = input("Введите число: ")
#     if N == 1:
#         return num
#     return revers_values(N-1) + f' {num}'
# print(revers_values(2))

# def reverse(list_1, index=1, final_list=[]):
#     length= len(list_1)
#     if index==length+1:
#         return final_list
#     final_list.append(list_1[length-index])
#     return reverse(list_1, index+1, final_list)

# list_2=['Вася','Петя','Серёжа','Игорь','Катя','Света']
# print(reverse(list_2))

# def reverse(arr):
#     if len(arr) > 0:
#         print(arr[-1], end=" ")
#         reverse(arr[:-1])
#     pass

# n = [3, 4, 5, 7]
# reverse(n)

# import random
# list_1 = list()
# for i in range (0, 5):
#     number = random.randint(1, 5)
#     list_1.append(number)
# print(list_1)
# min_num = min(list_1)
# max_num = max(list_1)
# for j in range(len(list_1)):
#     if list_1[j] == max_num:
#     list_1[j] = min_num
# print(list_1)

# def num(n):
#     if n == 0:
#         return
#     admin = int(input())
#     num(n - 1)
#     print(admin)

# n = int(input("Введите количество элементов последовательности: "))
# print("Введите последовательность:")
# num(n)