from socket import *
import json
import sys
import logging
import logs.client_log_config
from common.variables import ENCODING, MAX_PACKAGE_LENGTH
from common.actions import PRESENCE
from common.utils import create_parser

log = logging.getLogger('chat.client')


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

    msg = PRESENCE
    jim_msg = json.dumps(msg)
    s.send(jim_msg.encode(ENCODING))

    data = s.recv(MAX_PACKAGE_LENGTH)
    try:
        decode_data = data.decode(ENCODING)
        jim_data = json.loads(decode_data)
        print(f'Сообщение от сервера:\n{serv_answer_parsing(jim_data)}')
    except(ValueError, json.JSONDecodeError):
        log.error('Невозможно декодировать ответ от сервера')


if __name__ == '__main__':
    main()
