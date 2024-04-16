# import numpy

# numbers = numpy.array(list(range(1, 10)))
# print(numbers)
# numbers = numbers.reshape((3, 3)) # превращает в массим указанной размерности
# print(numbers)



""" Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""

""" ДЗ. Добавить в справочник возможность копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой."""

# contact_data = {
#     'first_name': None,
#     'second_name': None,
#     'phone_number': None
# }


# def ask_data():
#     s_name = input("Введите фамилия: ")
#     f_name = input("Введите имя: ")
#     m_name = input("Введите отчество: ")
#     phone = input("Введите номер телефона: ")
#     contact = {'second_name': s_name,
#                'first_name': f_name,
#                'middle_name': m_name,
#                'phone_number': phone}
#     return contact

# def add_new_contact():
#     contact = ask_data()
#     with open('phonebook.txt', 'a', encoding='utf-8') as file:
#         for value in contact.values():
#             file.write(value, delimiter=';')        
#         file.write('\n')
#     # return True

# def open_phonebook():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         for line in file:
#             print("\t\t".join(line.split(";")))

# def find_contact():
#     #print(f"Поиск по:\n1 фамилии\n2 имени\n3 отчеству\n4 номеру телефона\n0 выход")
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     s_name = input("Введите фамилию: ")
#     n_line = []
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         for counter, line in enumerate(file):
#             line = line.split()
#             if s_name in line[0]:
#                 n_line.append(counter)
#                 print("\t\t".join(line))
#     print(n_line)            
#     return n_line

# # def delete_contacr():
# #     # s_name = input("Введите фамилию: ")
# #     # with open('phonebook.txt', 'r', encoding='utf-8') as file:
# #     find_contact()

# def main():
#     isStop = 10
#     while isStop != 0:
#         print(f"Выберете, что хотите сделать:\n1 найти\n2 добавить\n3 сохранить\n4 открыть всю книгу\n5 копировать\n0 выход")
#         isStop = int(input(">"))
#         if isStop == 1:
#             find_contact()
#         elif isStop == 2:
#             add_new_contact()
#         elif isStop == 4:
#             open_phonebook()
#         input("Нажмите Enter, чтобы продолжить")
# main()

# /////////////////////////////////////////////////////////////////////////////////
import os
os.system("clear")
filename = 'guide.txt'

def add_tel():
    data = [
    input("Введите фамилию: "),
    input("Введите имя: "),
    input("Введите отчество: "),
    input("Введите номер телефона: "),
    ]
    st = " ".join(data)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(st+'\n')
    print('Номер записан!')
    return

# def get_guide(): #не работает
# data = []
# with open(filename, "r") as f:
# st = f.read()
# while st != " ":
# data.append([])
# data.append(st.split())
# st = f.read()
# for i in range(len(data)):
# print(*data[i])
# return data

def get_guide():
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        st = f.read()
    print(st)
    return data


def menu():
    dct = {
    "cr": 'Добавить запись (введите "cr")',
    "sh": 'Вывести справочник (введите "sh")',
    "ex": 'Выйти из программы (введите "ex")',
    }
    print("-", dct["cr"])
    print("-", dct["sh"])
    print("-", dct["ex"])
    cmd = input('Введите команду ')
    if cmd not in dct:
        print("Такой команды нет, выбирите другую")
        return -1
    else:
        return cmd


while True:
    cmd = menu()
    if cmd == "cr":
        add_tel()
    elif cmd == "sh":
        get_guide()
    else:
        exit()
    input('Нажмите enter, чтобы продолжить')
       
    # /////////////////////////////////////////////////////////////////////////////////