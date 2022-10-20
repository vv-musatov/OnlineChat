import platform
import subprocess
from chardet import detect

"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и 
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных."""


def task_1(*words):
    print('Задание № 1')

    for word in words:
        print(word, type(word))

    print('-' * 80)


"""Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом, 
а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы 
encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных."""


def task_2(*words):
    print('Задание № 2')

    for word in words:
        word = eval(f"b'{word}'")
        print(word, type(word), len(word))

    print('-' * 80)


"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. 
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем."""


def task_3(*words):
    print('Задание № 3')

    for word in words:
        try:
            word_bytes = word.encode('ascii')
            print(f'{word} - возможно записать в байтовом виде: {word_bytes}')
        except UnicodeEncodeError:
            print(f'{word} - невозможно записать в байтовом виде')

    print('-' * 80)


"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления 
в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""


def task_4(*words):
    print('Задание № 4')

    for word in words:
        enc_word = word.encode('utf-8')
        print(enc_word)
        dec_word = enc_word.decode('utf-8')
        print(dec_word)

    print('-' * 80)


"""Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат из 
байтового типа данных в строковый без ошибок для любой кодировки операционной системы."""


def task_5(*args):
    print('Задание № 5')

    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

    print('-' * 80)


"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной 
кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан."""


def task_6(*words):
    print('Задание № 5')

    file_name = 'test.txt'

    with open(file_name, 'w') as f_n:
        for word in words:
            f_n.write(word + '\n')
        f_n.close()

    with open(file_name, 'rb') as f_n:
        content = f_n.read()
        f_n.close()
    encoding = detect(content)['encoding']

    with open(file_name, encoding=encoding) as f_n:
        for el_str in f_n:
            print(el_str, end='')

    print('-' * 80)


def main():
    task_1('разработка', 'сокет', 'декоратор')
    task_1(
        '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
        '\u0441\u043e\u043a\u0435\u0442',
        '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    )
    task_2('class', 'function', 'method')
    task_3('attribute', 'класс', 'функция', 'type')
    task_4('разработка', 'администрирование', 'protocol', 'standard')
    task_5('ping', '-n' if platform.system().lower() == 'windows' else '-c', '2', 'yandex.ru')
    task_5('ping', '-n' if platform.system().lower() == 'windows' else '-c', '2', 'youtube.com')
    task_6('сетевое программирование', 'сокет', 'декоратор')


if __name__ == '__main__':
    main()
