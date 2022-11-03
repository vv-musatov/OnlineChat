import os
import sys
import logging

sys.path.append(os.path.join(os.getcwd(), '..'))

import logs.client_log_config
import logs.server_log_config
import traceback


def dec_log(func):
    def wrapper(*args, **kwargs):
        if sys.argv[0].endswith('client.py'):
            logger = logging.getLogger('chat.client')
        else:
            logger = logging.getLogger('chat.server')
        res = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} вызвана с аргументами {args} {kwargs}')
        logger.debug(f'Функция {func.__name__} вызвана из функции {traceback.extract_stack()[-2].name}')
        return res
    return wrapper
