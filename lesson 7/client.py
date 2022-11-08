from socket import *
import sys
import logging
import logs.client_log_config
from logs.dec_log import dec_log
from common.utils import create_parser, get_message, send_message

log = logging.getLogger('chat.client')


@dec_log
def msg_parsing(msg):
    log.info(f"Получено новое сообщение от {msg['from']}")
    if msg['action'] == 'msg':
        print(f"Получено сообщение: {msg['message']}")
    else:
        log.debug('Невозможно получить сообщение')


@dec_log
def serv_answer_parsing(data):
    log.info(f'Проверка ответа от сервера: {data}')
    if data['response'] == 200:
        return f'200 OK'
    return f'400 Bad Request'


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))

    while True:
        msg_parsing(get_message(s))


if __name__ == '__main__':
    main()
