"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла); Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в
соответствующий CSV-файл; Проверить работу программы через вызов функции write_to_csv().
"""

import glob
import csv
import numpy as np
import re
from chardet import detect


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        os_prod_list,
        os_name_list,
        os_code_list,
        os_type_list,
    ]
    headers = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    for f_n in glob.glob('*.txt'):
        with open(f_n, 'rb') as file:
            content = file.read()
            encode_content = detect(content)
            decode_content = content.decode(encode_content['encoding'])
            os_prod_list.append(re.compile(r'Изготовитель системы:\s*\S*').findall(decode_content)[0].split()[2])
            os_name_list.append(re.compile(r'Название ОС:\s*\S*').findall(decode_content)[0].split()[2])
            os_code_list.append(re.compile(r'Код продукта:\s*\S*').findall(decode_content)[0].split()[2])
            os_type_list.append(re.compile(r'Тип системы:\s*\S*').findall(decode_content)[0].split()[2])

    main_data = np.array(main_data, dtype=str).T.tolist()
    main_data.insert(0, headers)
    return main_data


def write_to_csv(data):
    with open('csv_result.csv', 'w', encoding='utf-8') as f_n:
        writer = csv.writer(f_n)
        for row in data:
            writer.writerow(row)


def main():
    write_to_csv(get_data())


if __name__ == '__main__':
    main()
