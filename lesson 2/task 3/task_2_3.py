"""
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое
число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €); Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
возможность работы с юникодом: allow_unicode = True; ВАЖНО: Реализовать считывание данных из созданного файла и
проверить, совпадают ли они с исходными.
"""

import yaml


def write_data_to_yaml():
    data = {
        'item': ['Монитор', 'Philips'],
        'quantity': 10,
        'prices': {
            'min_price': '100 €',
            'max_price': '200 €'
        }
    }

    with open('file.yaml', 'w', encoding='utf-8') as f_n:
        yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open('file.yaml', 'r', encoding='utf-8') as f_n:
        content = yaml.load(f_n, Loader=yaml.FullLoader)

    if content == data:
        print('Данные идентичны')
    else:
        print('Что-то пошло не так')


def main():
    write_data_to_yaml()


if __name__ == '__main__':
    main()
