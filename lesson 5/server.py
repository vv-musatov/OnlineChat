import json
import sys
import logging
import logs.server_log_config
from socket import *
from common.variables import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING
from common.utils import create_parser
from common.actions import RESPONSE_200, RESPONSE_400

log = logging.getLogger('chat.server')


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
            data = client.recv(MAX_PACKAGE_LENGTH)
            decode_data = data.decode(ENCODING)
            jim_data = json.loads(decode_data)
            print(f'Сообщение от клиента:\n{jim_data}')
            jim_response = json.dumps(client_answer_parsing(jim_data))
            client.send(jim_response.encode(ENCODING))
            client.close()
        except(ValueError, json.JSONDecodeError):
            log.error('Получено неверное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
