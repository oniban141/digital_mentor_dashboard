import requests
from datetime import datetime,timedelta
from app.services.auth_service import get_token_api
from app.utils.config import CRM_API_URL

def fetch_all_users():
    access_token = get_token_api()
    limit = 100
    offset = 0
    all_users = []

    while True:
        params = {
            'limit': limit,
            'offset': offset
        }

        headers = {
            "x-access-token": access_token,
            "Content-Type": "application/json"
        }

        response = requests.get(CRM_API_URL, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Ошибка: {response.status_code}, {response.text}")

        data = response.json()
        users = data.get('users', [])

        if not users:
            break

        all_users.extend(users)
        offset += limit

    return all_users

def get_pensioners_from_crm(days=30):
    all_users = fetch_all_users()
    today = datetime.now()
    date_threshold = today - timedelta(days=days)

    pensioners = [
        user for user in all_users
        if user.get("project") == "Цифровой наставник" and
           datetime.fromisoformat(user.get("createdAt").replace('Z', '+00:00')) >= date_threshold
    ]
    return pensioners
