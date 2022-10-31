import argparse
import os
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
    parser.add_argument('-p', '--port', default=DEFAULT_PORT, type=int)
    return parser
