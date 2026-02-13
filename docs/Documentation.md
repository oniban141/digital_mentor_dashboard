Бэкенд
config_utils.py
Хранит конфигурационные данные для подключения к API

crm_service.py
Содержит функции для работы с API "МойКласс":
get_token_api()
Получает токен для доступа к API

fetch_all_users()
Получает всех пользователей (пенсионеров) из API

fetch_all_managers()
Получает всех менеджеров (волонтеров) из API

data_processing.py
Содержит функции для обработки данных

get_current_metrics()
Получает текущие метрики

get_history_data()
Получает исторические данные

dashboard_data.py
Содержит API эндпоинты

main.py
Основной файл FastAPI

api_client.js
Клиент для работы с API

main.js
Основной JavaScript

Запуск проекта


Соберите Docker-контейнер:
cd backend
docker build -t dashboard-backend .

Запустите Docker-контейнер:
docker run -p 8000:8000 dashboard-backend

Откройте фронтенд:
Откройте файл frontend/index.html в вашем браузере.

