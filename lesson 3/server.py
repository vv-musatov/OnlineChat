import json
import sys
from socket import *
from common.variables import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING
from common.utils import create_parser
from common.actions import RESPONSE_200, RESPONSE_400


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
        data = client.recv(MAX_PACKAGE_LENGTH)
        decode_data = data.decode(ENCODING)
        jim_data = json.loads(decode_data)
        print(f'Сообщение от клиента:\n{jim_data}')
        if jim_data['action'] == 'presence':
            response = RESPONSE_200
        else:
            response = RESPONSE_400

        jim_response = json.dumps(response)
        client.send(jim_response.encode(ENCODING))


if __name__ == '__main__':
    main()
