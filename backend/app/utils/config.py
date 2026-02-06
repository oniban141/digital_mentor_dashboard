import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_AUTH = os.getenv("URL_AUTH", "https://api.moyklass.com/v1/company/auth/getToken")
CRM_API_URL = os.getenv("CRM_API_URL", "https://api.moyklass.com/v1/company/users")
