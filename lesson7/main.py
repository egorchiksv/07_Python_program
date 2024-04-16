"""Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284"""

# number = 10000


# def friendlyNumber(num):
#         out=0
#         for div in range(1, num):
#             if num%div==0:
#                 out+=div
#         return out


# for current_num in range (2, number):
#     m=friendlyNumber(current_num)
#     n=friendlyNumber(m)
#     if n==current_num and n <m:
#         print(n,' ',m)

# def sum_dev(n):
#         res = 0
#         for i in range(1, int(n/2) + 1):
#             if n % i == 0:
#                 res += i
#         return res

# k = 1400
# for i in range(1, k):
#     for j in range(i + 1, k):
#         if sum_dev(j) == i and sum_dev(i) == j:
#             print(i, j)

# def sum_div(n):
#     res = 1 # Инициализация результата с 1, так как 1 делитель у любого числа
#     i = 2 # Начинаем с 2, так как 1 уже включено в сумму
#     while i * i <= n:
#         if n % i == 0:
#             res += i
#     if i != n // i: # Проверяем, чтобы не учитывать квадратный корень дважды
#         res += n // i
#         i += 1
#     return res

# k = 10000
# div_sum = [sum_div(n) for n in range(k)] # Заранее вычисляем суммы делителей для всех чисел до k

# for i in range(1, k):
#     if div_sum[i] < k and i != div_sum[i] and div_sum[div_sum[i]] == i:
#         print(i, div_sum[i])

"""import random
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 100))
# можно записать как
import random
numbers = [random.randint(1, 100) for i in range(5)]

def is_odd(number:int):
    if number % 2 == 1:
        return False
    return True
# можно записать как
is_odd = lambda number: False if number % 2 else True

# можно записать как
numbers = list(filter(is_odd, numbers))

numbers = [2, 4, 6, 8, 10, 12]
carbons = [58, 46, 34, 22, 10, 8]
union = []
for num1, num2 in zip(numbers, carbons):
    union.append(num1 + num2)

from math import factorial
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
factorials = list(map(factorial, numbers))"""

"""Задача №47. У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы
используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.
Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print(‘ok’)
else:
 print(‘fail’)
Вывод:
ok"""

# trasformation = lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

#transformed_values = lambda x: x # тоже самое, что def func (x):
                                                    # return x

"""Задача №49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
Пример ввода и вывода данных представлены на следующем слайде
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10"""

# print(list(enumerate(orbits))) # выводит нумерованный список, делает картеж в картеже
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] # список из картежей
# print(orbits[2][0]) # берем из списка одно число из картежа

# from math import pi # Взять число Пи из библеотеки math

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#     s_orbits = list(map(lambda i: i[0]*i[1]*pi if i[0]!=i[1] else 0, orbits))
#     max_index = s_orbits.index(max(s_orbits))
#     return orbits[max_index]

# print(find_farthest_orbit(orbits))

#print(*find_farthest_orbit(orbits))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def crass_section(pair):
#     if pair[0] != pair[1]:
#         return pi*pair[0]*pair[1]
#     else:
#         return 0

# def find_farthest_orbit(orbits):
#     list_orbit_space = list(map(crass_section, orbits))
#     index_max=list_orbit_space.index(max(list_orbit_space))
#     return orbits[index_max]

# print(*find_farthest_orbit(orbits))

# def find_farthest_orbit(orb):
#     return max(orb, key=lambda x: pi * x[0] * x[1] if x[0] != x[1] else 0)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits)) # * позволяет вывести каждое отдельное число

"""Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)"""

# def same_by(characteristic, objects):
#     if not objects:
#         return True
# #    characteristics = [characteristic(obj) for obj in objects]
#     return len(set(map(characteristic, objects))) in [0, 1]

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

# def same_by(characteristic, objects):
#     arr = [characteristic(el) for el in objects]
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i - 1]:
#             return False
#     return True

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")
    
# def same_by(function, value):
#     if len(value) ==0:
#         return True
#     out=list(filter(function, value))
#     return len(value)==len(out)


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')

# def same_by(characteristic, value):
#     if len(value) ==0:
#         return True
#     out=list(filter(characteristic, value))
#     return len(value)==len(out)


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')

# print(2 > 3)
# print(5 == 7)
# print(5 in [5, 6])