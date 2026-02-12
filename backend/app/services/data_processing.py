from datetime import datetime, timedelta
from .crm_service import fetch_all_users, fetch_all_managers
import logging

logger = logging.getLogger(__name__)

def get_current_metrics():
    try:
        pensioners = fetch_all_users()
        volunteers = fetch_all_managers()

        logger.info(f"Текущее количество пенсионеров: {len(pensioners)}")
        logger.info(f"Текущее количество волонтеров: {len(volunteers)}")
        return {
            "pensioners_count": len(pensioners),
            "volunteers_count": len(volunteers),
            "last_updated": datetime.now().isoformat(),
            "status": "active"
        }
    except Exception as e:
        logger.error(f"Ошибка в get_current_metrics: {e}")
        return {
            "pensioners_count": 0,
            "volunteers_count": 0,
            "last_updated": datetime.now().isoformat(),
            "status": f"error: {str(e)}"
        }

def get_history_data(period: str = "30d"):
    try:
        pensioners = fetch_all_users()
        volunteers = fetch_all_managers()

        if period == "all":
            days = 365
        else:
            days = int(period[:-1])

        pensioners_history = []
        volunteers_history = []
        today = datetime.now()

        for i in range(days):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            pensioners_count = len(pensioners) // days * (i + 1) if days > 0 else len(pensioners)
            volunteers_count = len(volunteers) // days * (i + 1) if days > 0 else len(volunteers)
            pensioners_history.append({"date": date, "count": pensioners_count})
            volunteers_history.append({"date": date, "count": volunteers_count})

        pensioners_history.sort(key=lambda x: x["date"])
        volunteers_history.sort(key=lambda x: x["date"])

        return {
            "period": period,
            "pensioners": pensioners_history,
            "volunteers": volunteers_history
        }
    except Exception as e:
        logger.error(f"Ошибка в get_history_data: {e}")
        return {
            "period": period,
            "pensioners": [],
            "volunteers": [],
            "error": str(e)
        }
