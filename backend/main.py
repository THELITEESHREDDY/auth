from fastapi import FastAPI,APIRouter
from backend.config.db_config import create_db_and_tables
from backend.auth import routers 
from fastapi.middleware.cors import CORSMiddleware
from backend.config.settings import settings

app = FastAPI(
    title="authbackend",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
app.include_router(routers.router)

@app.get("/health")
async def hello():
    return {"message":"Hello Big Application"}