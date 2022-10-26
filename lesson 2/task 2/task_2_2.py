"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа; Проверить работу программы через
вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', 'r', encoding='utf-8') as f_n:
        content = json.load(f_n)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        content['orders'].append(order)
        json.dump(content, f_n, indent=4, ensure_ascii=False)


def main():
    write_order_to_json('Монитор', '10', '15000', 'ООО "Компания"', '20.10.2022')
    write_order_to_json('Клавиатура', '50', '8000', 'ООО "Организация"', '20.10.2022')


if __name__ == '__main__':
    main()
