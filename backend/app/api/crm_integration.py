from fastapi import APIRouter, HTTPException
from app.services.crm_service import fetch_all_users
from datetime import datetime

router = APIRouter()

@router.get("/sync")
async def sync_crm_data():
    try:
        today = datetime.now()
        date_from = (today - datetime(days=30)).strftime("%m.%d.%Y")
        date_to = today.strftime("%m.%d.%Y")
        data = fetch_all_users(date_from, date_to)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
