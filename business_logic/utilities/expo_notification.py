import requests
import json


def send_push_message(token, username, destination, extra=None):
    url = 'https://exp.host/--/api/v2/push/send'
    data = {
        "to": token,
        "title": "Request Approved",
        "body": "Hello " + username + ", your request to "+destination + " has been approved",
        'sound': 'default',
        # 'data': {'someData': 'goes here'},
    }

    try:
        response = requests.post(
            url, data=data)
        return response.json()
    except Exception as exception:
        raise exception


# send_push_message('ExponentPushToken[J0YkqmGwt6jwk2SzhgRrN1]', 'sds', 'hfj')
