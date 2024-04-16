""" Задача №9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120

number = int(input("Введите число: "))
factorial = 1
while number >= 1:
    print(number)
    factorial *= number
    print(f"Приумножили факториал на {number}. Получилось {factorial}")
    number -= 1
print(factorial)"""

""" Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6"""

# A = int(input("Введите число: "))
# temp = 0
# n1 = 1
# n2 = 1
# count = 2 # Т.к. первые числа известны
# while temp <= A:
#     temp = n1 + n2 # сложили два последних
#     n1 = n2 # перенесли предпоследнее
#     n2 = temp # вместо предпоследнего записали последнее
#     count += 1
#     if temp > A:
#         count = 0
# if count != 0:
#     print(count)
# else:
#     print(-1)

# number = int(input("Введите число: "))
# fibonacci = 0
# f0 = 0
# f1 = 1
# i = 2
# if number == 0:
# print(f"Число ({number}) является 1 по счету в числовой последовательности Фибоначи")
# elif number == 1:
# print(f"Число ({number}) является 2 по счету в числовой последовательности Фибоначи")
# else:
# while number > fibonacci:
# fibonacci = f1 + f0
# f0 = f1
# f1 = fibonacci
# i += 1
# if number == fibonacci:
# print(f"Число ({number}) является ({i}) по счету в числовой последовательности Фибоначи")
# else:
# print(f"Число ({number}) не является элементом числовой последовательности Фибоначи")

# x = int(input("Введите число: "))
# a, b = 0, 1
# n = 1
# count = 1
# while n <= x:
# n = a + b
# a, b = b, n
# count += 1

# if x == 1:
# print(2,3)
# elif x == 0:
# print(1)
# elif x == a:
# print(count)
# else:
# print(-1)

A = int(input("введите число :"))
f0=0
f1=1
f=f1
i=0
while f<=A:
f=f0+f1
f0,f1=f1,f # в f0 заносится f1 и в f1 заносится f
i+=1
if f0==A :
print(i+1)
else:
print(-1)