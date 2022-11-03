import json
import sys
import logging
import logs.server_log_config
from logs.dec_log import dec_log
from socket import *
from common.variables import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING
from common.utils import create_parser, get_message, send_message
from common.actions import RESPONSE_200, RESPONSE_400

log = logging.getLogger('chat.server')


@dec_log
def client_answer_parsing(data):
    log.info(f"Проверка ответа от клиента: {data['action']}")
    if data['action'] == 'presence':
        return RESPONSE_200
    return RESPONSE_400


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(MAX_CONNECTIONS)

    while True:
        client, client_addr = s.accept()
        try:
            jim_msg = get_message(client)
            print(f'Сообщение от клиента:\n{jim_msg}')
            jim_response = client_answer_parsing(jim_msg)
            send_message(client, jim_response)
            client.close()
        except(ValueError, json.JSONDecodeError):
            log.error('Получено неверное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
