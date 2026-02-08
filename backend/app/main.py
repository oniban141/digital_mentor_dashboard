from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import dashboard_data, crm_integration
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_data.router, prefix="/api/dashboard")
app.include_router(crm_integration.router, prefix="/api/crm")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")

@app.get("/")
async def root():
    return {"message": "Welcome to Digital Mentor Dashboard API"}
