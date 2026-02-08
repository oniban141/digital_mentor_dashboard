from datetime import datetime, timedelta
from app.services.crm_service import get_pensioners_from_crm
from fastapi import HTTPException
from functools import lru_cache
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def get_current_metrics():
    try:
        logger.info("Fetching current metrics...")
        pensioners = get_pensioners_from_crm(days=30)
        return {
            "current_count": len(pensioners),
            "last_updated": datetime.now().isoformat(),
            "status": "active"
        }
    except Exception as e:
        logger.error(f"Error fetching metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@lru_cache(maxsize=1)
def get_history_data(period: str = "7d"):
    try:
        logger.info(f"Fetching history data for period {period}...")
        days = int(period[:-1])
        pensioners = get_pensioners_from_crm(days=days)
        total_pensioners = len(pensioners)

        history = []
        today = datetime.now()
        for i in range(days):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            count = total_pensioners // days
            if i < total_pensioners % days:
                count += 1
            history.append({"date": date, "count": count})

        history.sort(key=lambda x: x["date"])
        return {"period": period, "data": history}
    except Exception as e:
        logger.error(f"Error fetching history data: {e}")
        raise HTTPException(status_code=500, detail=str(e))
