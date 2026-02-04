from fastapi import APIRouter, HTTPException
from app.services.crm_service import fetch_crm_data

router = APIRouter()

@router.get("/sync")
async def sync_crm_data():
    try:
        data = fetch_crm_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
