from fastapi import FastAPI,APIRouter
from backend.config.db_config import create_db_and_tables
from backend.auth import routers 
app = FastAPI(
    title="authbackend",
    version="0.1.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
app.include_router(routers.router)

@app.get("/health")
async def hello():
    return {"message":"Hello Big Application"}