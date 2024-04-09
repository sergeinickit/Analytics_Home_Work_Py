'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
import csv
from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    last_name = "Ivanov"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name): 
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Номер'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Номер"] == str(lst[2]):
            print("Такой Номер уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Номер": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


file_name = 'phone.csv'


def transfer_data(source: str, dest: str, num_row: int):   
    num_row = int(num_row)
    if not exists(source):
        print("Исходный файл не существует.")
        return
    with open(source,"r", encoding='utf-8') as data:
        reader = csv.DictReader(data)
        rows = list(reader)
        if 0 < num_row < len(rows):
            row_to_copy = rows[num_row - 1]
            with open(dest, "w", encoding='utf-8', newline='') as data_2:
                fieldnames = ['Имя', 'Фамилия', 'Номер']
                writer = csv.DictWriter(data_2, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(row_to_copy)
        else:
            print("Некорректный номер строки")
            
data_2 = "NewPhone.csv"
            


def main():
    while True:

        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))  
        elif command == "c":
            num_row = input("Введите номер строки: ")
            transfer_data(file_name, data_2, num_row)

main()