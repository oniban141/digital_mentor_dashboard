from fastapi import APIRouter, HTTPException
from app.services.crm_service import fetch_all_users

router = APIRouter()

@router.get("/sync")
async def sync_crm_data():
    try:
        data = fetch_all_users()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
