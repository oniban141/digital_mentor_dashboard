import requests
from ..utils.config import API_KEY, URL_AUTH, USERS_API_URL, MANAGERS_API_URL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_token_api():
    post_auth = {'apiKey': API_KEY}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(URL_AUTH, json=post_auth, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()['accessToken']
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка аутентификации: {e}")
        raise Exception(f"Ошибка аутентификации: {e}")

def fetch_all_users():
    try:
        access_token = get_token_api()
        limit = 100
        offset = 0
        all_users = []

        while True:
            params = {'limit': limit, 'offset': offset}
            headers = {"x-access-token": access_token, "Content-Type": "application/json"}

            try:
                response = requests.get(USERS_API_URL, headers=headers, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()
                users = data.get('users', [])

                if not users:
                    break

                all_users.extend(users)
                offset += limit
            except requests.exceptions.RequestException as e:
                logger.error(f"Ошибка при получении пользователей: {e}")
                raise Exception(f"Ошибка при получении пользователей: {e}")

        logger.info(f"Получено {len(all_users)} пенсионеров")
        return all_users
    except Exception as e:
        logger.error(f"Ошибка в fetch_all_users: {e}")
        raise e

def fetch_all_managers():
    try:
        access_token = get_token_api()
        limit = 100
        offset = 0
        all_managers = []

        while True:
            params = {'limit': limit, 'offset': offset}
            headers = {"x-access-token": access_token, "Content-Type": "application/json"}

            try:
                response = requests.get(MANAGERS_API_URL, headers=headers, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()
                managers = data.get('managers', [])

                if not managers:
                    break

                all_managers.extend(managers)
                offset += limit
            except requests.exceptions.RequestException as e:
                logger.error(f"Ошибка при получении менеджеров: {e}")
                raise Exception(f"Ошибка при получении менеджеров: {e}")

        logger.info(f"Получено {len(all_managers)} волонтеров")
        return all_managers
    except Exception as e:
        logger.error(f"Ошибка в fetch_all_managers: {e}")
        raise e
