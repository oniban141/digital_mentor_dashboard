import requests
from app.utils.config import CRM_API_TOKEN, CRM_API_URL

def fetch_crm_data():
    headers = {"Authorization": f"Bearer {CRM_API_TOKEN}"}
    response = requests.get(f"{CRM_API_URL}/v1/company/users", headers=headers)
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")
    if response.status_code != 200:
        raise Exception(f"Ошибка CRM: {response.status_code}")
    return response.json()


def get_pensioners_from_crm():
    """Фильтрация пенсионеров по проекту 'Цифровой наставник'."""
    data = fetch_crm_data()
    pensioners = [user for user in data if user.get("project") == "Цифровой наставник"]
    return pensioners
