import json
import time
from socket import *
import sys
import logging
import logs.client_log_config
import threading
from logs.dec_log import dec_log
from common.utils import create_parser, get_message, send_message

log = logging.getLogger('chat.client')


@dec_log
def create_presence(client_name):
    msg = {
        'action': 'presence',
        'time': time.time(),
        'type': 'status',
        'user': {
            'account_name': client_name,
            'status': 'I am here!'
        }
    }
    return msg


@dec_log
def serv_answer_parsing(data):
    log.info(f'Проверка ответа от сервера: {data}')
    if data['response'] == 200:
        return f'200 OK'
    return f'400 Bad Request'


@dec_log
def message_from_server(s, username):
    while True:
        try:
            msg = get_message(s)
            if msg['action'] == 'msg' and msg['to'] == username:
                print(f"\nПолучено сообщение от {msg['from']}"
                      f"\n{msg['text']}")
        except (OSError, ConnectionError, ConnectionAbortedError, json.JSONDecodeError):
            log.debug('Соединение потеряно')


@dec_log
def create_msg(s, account_name):
    to_user = input('Введите получателя: ')
    msg = input('Введите сообщение: ')
    msg_dict = {
        'action': 'msg',
        'from': account_name,
        'to': to_user,
        'time': time.time(),
        'text': msg
    }
    try:
        send_message(s, msg_dict)
    except:
        sys.exit(1)


@dec_log
def user_interactive(s, username):
    print('Команды: ',
          '\n 1. msg - отправить сообщение',
          '\n 2. exit - выход')
    while True:
        cmd = input('Введите команду: ')
        if cmd == 'msg':
            create_msg(s, username)
        elif cmd == 'exit':
            time.sleep(0.5)
            break
        else:
            print('Некорректный ввод')


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    client_name = namespace.name
    print(f'Имя пользователя {client_name}')

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))
    send_message(s, create_presence(client_name))

    receiver = threading.Thread(target=message_from_server, args=(s, client_name))
    receiver.daemon = True
    receiver.start()

    user_interface = threading.Thread(target=user_interactive, args=(s, client_name))
    user_interface.daemon = True
    user_interface.start()

    while True:
        time.sleep(1)
        if receiver.is_alive() and user_interface.is_alive():
            continue
        break


if __name__ == '__main__':
    main()
