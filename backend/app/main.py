from fastapi import FastAPI
from .api import api_router

app = FastAPI(
    title="API Mi Proyecto",
    version="0.1.0"
)

app.include_router(api_router)

