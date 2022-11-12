import time
from socket import *
import sys
import logging
import logs.client_log_config
from logs.dec_log import dec_log
from common.utils import create_parser, send_message

log = logging.getLogger('chat.client')


@dec_log
def create_message(s):
    text = input('Введите сообщение: ')
    if text == 'exit':
        s.close()
        sys.exit(0)
    msg = {
        'action': 'msg',
        'time': time.time(),
        'from': 'wk',
        'message': text
    }
    return msg


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))

    while True:
        send_message(s, create_message(s))


if __name__ == '__main__':
    main()
