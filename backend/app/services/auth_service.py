import requests
from app.utils.config import API_KEY, URL_AUTH, REQUEST_TIMEOUT

def get_token_api():
    headers = {"Content-Type": "application/json"}
    post_auth = {"apiKey": API_KEY}

    try:
        response = requests.post(URL_AUTH, json=post_auth, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()['accessToken']
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка аутентификации: {e}")
