# import os

# # Настройки для подключения к API МойКласс
# CRM_API_URL = "https://api.moyklass.com"
# CRM_API_TOKEN = os.getenv("apiKey", "013ZGtSaee7r5Zrj0Q89wY66YkOeG3BuX8kB2ljS8OIcWi8lrfoS")
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("013ZGtSaee7r5Zrj0Q89wY66YkOeG3BuX8kB2ljS8OIcWi8lrfoS")
URL_AUTH = os.getenv("URL_AUTH", "https://api.moyklass.com/v1/company/auth/getToken")
CRM_API_URL = os.getenv("CRM_API_URL", "https://api.moyklass.com")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))
