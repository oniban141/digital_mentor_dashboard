from fastapi import APIRouter, HTTPException
from app.services.data_processing import get_current_metrics, get_history_data
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/metrics")
async def get_metrics():
    try:
        metrics = get_current_metrics()
        return metrics
    except Exception as e:
        logger.error(f"Error in /metrics endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def get_history(period: str = "7d"):
    try:
        history = get_history_data(period)
        return history
    except Exception as e:
        logger.error(f"Error in /history endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
