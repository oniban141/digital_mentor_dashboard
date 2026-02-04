from datetime import datetime, timedelta
from app.services.crm_service import get_pensioners_from_crm

# Кеш в памяти
_cached_metrics = None
_cached_history = None

def get_current_metrics():
    """Получение текущей метрики."""
    global _cached_metrics
    pensioners = get_pensioners_from_crm()
    _cached_metrics = {
        "current_count": len(pensioners),
        "last_updated": datetime.now().isoformat(),
        "status": "active"
    }
    return _cached_metrics

def get_history_data(period: str = "7d"):
    """Получение исторических данных для графика."""
    global _cached_history
    pensioners = get_pensioners_from_crm()

    # Пример: генерация тестовых данных
    history = []
    today = datetime.now()
    for i in range(7):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        history.append({"date": date, "count": len(pensioners) - i * 10})

    _cached_history = {"period": period, "data": history}
    return _cached_history
