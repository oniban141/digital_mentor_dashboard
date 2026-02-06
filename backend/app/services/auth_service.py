import requests
from app.utils.config import API_KEY, URL_AUTH

def get_token_api():
    post_auth = {'apiKey': API_KEY}

    response = requests.post(
        URL_AUTH,
        json=post_auth,
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        return response.json()['accessToken']
    else:
        raise Exception(f"Ошибка: {response.status_code}, {response.text}")
