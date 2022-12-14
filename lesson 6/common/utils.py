import argparse
import os
import sys
import json

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ENCODING, MAX_PACKAGE_LENGTH
from logs.dec_log import dec_log


@dec_log
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
    parser.add_argument('-p', '--port', default=DEFAULT_PORT, type=int)
    return parser


@dec_log
def get_message(sock):
    data = sock.recv(MAX_PACKAGE_LENGTH)
    decode_data = data.decode(ENCODING)
    jim_data = json.loads(decode_data)
    return jim_data


@dec_log
def send_message(sock, msg):
    jim_msg = json.dumps(msg)
    sock.send(jim_msg.encode(ENCODING))
