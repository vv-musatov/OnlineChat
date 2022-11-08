import sys
import logging
import select
import time
import logs.server_log_config
from logs.dec_log import dec_log
from socket import *
from common.variables import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING
from common.utils import create_parser, get_message, send_message
from common.actions import RESPONSE_200, RESPONSE_400

log = logging.getLogger('chat.server')


@dec_log
def client_answer_parsing(data, msg_list):
    log.info(f"Проверка ответа от клиента: {data['action']}")
    if data['action'] == 'presence':
        return RESPONSE_200
    elif data['action'] == 'msg':
        msg_list.append((data['from'], data['message']))
        return
    return RESPONSE_400


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.settimeout(0.5)

    clients = []
    messages = []

    s.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_addr = s.accept()
        except OSError as e:
            pass
        else:
            clients.append(client)

        read_lst = []
        write_lst = []

        try:
            if clients:
                read_lst, write_lst, _ = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if read_lst:
            for client_msg in read_lst:
                try:
                    client_answer_parsing(get_message(client_msg), messages)
                except:
                    clients.remove(client_msg)

        if messages and write_lst:
            msg = {
                'action': 'msg',
                'from': messages[0][0],
                'time': time.time(),
                'message': messages[0][1]
            }
            del messages[0]
            for waiting_client in write_lst:
                try:
                    send_message(waiting_client, msg)
                except:
                    waiting_client.close()
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()
