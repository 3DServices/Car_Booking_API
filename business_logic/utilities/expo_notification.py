import requests
import json


def send_push_message(token, extra=None):
    url = 'https://exp.host/--/api/v2/push/send'
    data = {
        "to": token,
        "title": "hello",
        "body": "world",
        'sound': 'default',
        # 'data': {'someData': 'goes here'},
    }

    try:
        response = requests.post(
            url, data=data)
        print(response.json())
        return response.json()
    except Exception as exception:
        raise exception


# send_push_message('ExponentPushToken[J0YkqmGwt6jwk2SzhgRrN1]', 'sds', 'hfj')
