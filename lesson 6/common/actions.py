import time

PRESENCE = {
    'action': 'presence',
    'time': time.time(),
    'type': 'status',
    'user': {
        'account_name': 'wk',
        'status': 'I am here!'
    }
}

RESPONSE_200 = {
    'response': 200,
    'alert': 'OK'
}

RESPONSE_400 = {
    'response': 400,
    'error': 'Bad Request'
}
