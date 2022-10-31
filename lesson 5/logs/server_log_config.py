import logging
import logging.handlers
import os

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server.log')

formatter = logging.Formatter('%(asctime)s %(levelname)-6s %(module)-8s %(message)s')

log_hand = logging.handlers.TimedRotatingFileHandler(path, when='D', interval=1, encoding='utf-8')
log_hand.setFormatter(formatter)

log = logging.getLogger('chat.server')
log.addHandler(log_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    log.debug('Проверка отладочной информации')
    log.info('Проверка информационных сообщений')
    log.warning('Проверка предупреждений')
    log.error('Проверка ошибок')
    log.critical('Проверка критических ошибок/сообщений')
