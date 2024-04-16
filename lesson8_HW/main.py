""" ДЗ. Добавить в справочник возможность копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой."""
contact_data = {
    'first_name': None,
    'second_name': None,
    'phone_number': None
}


def ask_data():
    s_name = input("Введите фамилия: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
               'first_name': f_name,
               'middle_name': m_name,
               'phone_number': phone}
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value + '; ')
        file.write('\n')

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print('| {:8} | {:12} | {:20} | {:15} |'.format(*line.split(";")))


def find_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    search = input("Введите фамилию, имя, отчество или номер телефона: ")
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        n_line = []
        print("\t\t".join(title))
        for counter, line in enumerate(file):
            line = line.split(";")
            if search in line[0] or search in line[1] or search in line[2] or search in line[3]:
                n_line.append(counter)
                n_line.append(line)
                print(counter, '| {:8} | {:12} | {:20} | {:15} |'.format(*line))
    return n_line

def delete_contact():
    find_contact()
    num_str = int(input("Выберите номер записи, которую необходимо удалить: "))
    i = 0
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if i == num_str:
                break
            i += 1
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        f = file.read()
        new_line = f.replace(line, "")
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(new_line)

def copy_phonebook():
    copy = find_contact()
    num_str = int(input("Выберите номер записи, которую необходимо скопировать в файл: "))
    i = 0
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if i == (num_str - 1):
                with open('phonebook_copy.txt', 'a', encoding='utf-8') as file:
                    file.write(line)
            i += 1

def replace_contact():
    p = find_contact()
    num_str = int(input("Выберите номер записи, данные которой необходимо изменить: "))
    i = 0
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if i == num_str:
                break
            i += 1
    contact = ask_data()
    r_line = ''
    for value in contact.values():
        r_line += value + '; '
    r_line +='\n'
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        f = file.read()
        new_line = f.replace(line, r_line)
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(new_line)

def main():
    isStop = 10
    while isStop != 0:
        print(f"Выберете, что хотите сделать:\n1 найти\n2 добавить\n3 удалить\n4 открыть всю книгу\n5 копировать в новый файл\n6 изменить контакт\n0 выход")
        isStop = int(input(">"))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 3:
            delete_contact()
        elif isStop == 4:
            open_phonebook()
        elif isStop == 5:
            copy_phonebook()
        elif isStop == 6:
            replace_contact()
        input("Нажмите Enter, чтобы продолжить")
main()