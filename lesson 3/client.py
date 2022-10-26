from socket import *
import json
import sys
from common.variables import ENCODING, MAX_PACKAGE_LENGTH
from common.actions import PRESENCE
from common.utils import create_parser


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
    decode_data = data.decode(ENCODING)
    jim_data = json.loads(decode_data)
    print(f'Сообщение от сервера:\n{jim_data}')


if __name__ == '__main__':
    main()
