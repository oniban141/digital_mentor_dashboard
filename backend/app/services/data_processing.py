from datetime import datetime, timedelta
from app.services.crm_service import get_pensioners_from_crm

def get_current_metrics():
    pensioners = get_pensioners_from_crm(days=30)
    return {
        "current_count": len(pensioners),
        "last_updated": datetime.now().isoformat(),
        "status": "active"
    }

def get_history_data(period: str = "7d"):
    days = int(period[:-1])
    pensioners = get_pensioners_from_crm(days=days)
    total_pensioners = len(pensioners)

    history = []
    today = datetime.now()
    for i in range(days):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        # Распределяем пенсионеров равномерно по дням
        count = total_pensioners // days
        if i < total_pensioners % days:
            count += 1
        history.append({"date": date, "count": count})

    # Сортируем данные по дате
    history.sort(key=lambda x: x["date"])
    return {"period": period, "data": history}
