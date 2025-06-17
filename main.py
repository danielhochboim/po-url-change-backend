from fastapi import FastAPI
from routers.channels_router import router

app = FastAPI()

app.include_router(router, prefix="/channels")