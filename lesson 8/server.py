import sys
import logging
import select
import time
import logs.server_log_config
from logs.dec_log import dec_log
from socket import *
from common.variables import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING
from common.utils import create_parser, get_message, send_message, send_message_to_client
from common.actions import RESPONSE_200, RESPONSE_400

log = logging.getLogger('chat.server')


@dec_log
def client_answer_parsing(data, msg_list, client, clients, names):
    log.info(f"Проверка ответа от клиента: {data['action']}")
    if data['action'] == 'presence':
        if data['user']['account_name'] not in names.keys():
            names[data['user']['account_name']] = client
        return
    elif data['action'] == 'msg':
        msg_list.append(data)
        return
    return RESPONSE_400


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((addr, port))
    s.settimeout(0.5)

    clients = []
    messages = []
    names = dict()

    s.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_addr = s.accept()
        except OSError:
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
                    client_answer_parsing(get_message(client_msg), messages, client_msg, clients, names)
                except:
                    clients.remove(client_msg)

        for i in messages:
            try:
                send_message_to_client(i, names, write_lst)
            except:
                clients.remove(names[i['to']])
                del names[i['to']]
        messages.clear()


if __name__ == '__main__':
    main()
