from fastapi import APIRouter
from ..services.data_processing import get_current_metrics, get_history_data

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    metrics = get_current_metrics()
    return metrics

@router.get("/history")
async def get_history(period: str = "30d"):
    history = get_history_data(period)
    return history
