import os
from data_create import name_data, surname_data, phone_data, address_data
def load_data(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    records = []
    if filename == 'data_first_variant.csv':
        record = {}
        for line in data:
            if line.strip():
                if not record.get('name'):
                    record['name'] = line.strip()
                elif not record.get('surname'):
                    record['surname'] = line.strip()
                elif not record.get('phone'):
                    record['phone'] = line.strip()
                else:
                    record['address'] = line.strip()
            else:
                records.append(record)
                record = {}
    elif filename == 'data_second_variant.csv':
        for line in data:
            if line.strip():
                parts = line.strip().split(';')
                if len(parts) == 4:
                    records.append({
                        'name': parts[0],
                        'surname': parts[1],
                        'phone': parts[2],
                        'address': parts[3]
                    })
    return records

def save_data(records, filename, variant):
    with open(filename, 'w', encoding='utf-8') as f:
        for record in records:
            if variant == 1:
                f.write(f"{record['name']}\n{record['surname']}\n{record['phone']}\n{record['address']}\n\n")
            elif variant == 2:
                f.write(f"{record['name']};{record['surname']};{record['phone']};{record['address']}\n")

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        filename = 'data_first_variant.csv'
    elif var == 2:
        filename = 'data_second_variant.csv'

    records = load_data(filename)
    records.append({'name': name, 'surname': surname, 'phone': phone, 'address': address})
    save_data(records, filename, var)

def print_data():
    print('Вывожу данные из 1 файла: \n')
    records = load_data('data_first_variant.csv')
    for record in records:
        print(f"{record['name']}\n{record['surname']}\n{record['phone']}\n{record['address']}\n")

    print('Вывожу данные из 2 файла: \n')
    records = load_data('data_second_variant.csv')
    for record in records:
        print(f"{record['name']};{record['surname']};{record['phone']};{record['address']}\n")

def modify_data():
    var = int(input(f"Из какого файла изменить данные?\n\n"
                    f"1 Вариант: \n"
                    f"2 Вариант: \n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        filename = 'data_first_variant.csv'
    elif var == 2:
        filename = 'data_second_variant.csv'

    records = load_data(filename)
    print_data()
    entry_index = int(input('Введите номер записи для изменения: ')) - 1

    if 0 <= entry_index < len(records):
        record = records[entry_index]
        print(f"Текущие данные: {record}")
        record['name'] = name_data()
        record['surname'] = surname_data()
        record['phone'] = phone_data()
        record['address'] = address_data()
        save_data(records, filename, var)
    else:
        print("Неправильный номер записи")

def delete_data():
    var = int(input(f"Из какого файла удалить данные?\n\n"
                    f"1 Вариант: \n"
                    f"2 Вариант: \n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        filename = 'data_first_variant.csv'
    elif var == 2:
        filename = 'data_second_variant.csv'

    records = load_data(filename)
    print_data()
    entry_index = int(input('Введите номер записи для удаления: ')) - 1

    if 0 <= entry_index < len(records):
        del records[entry_index]
        save_data(records, filename, var)
    else:
        print("Неправильный номер записи")