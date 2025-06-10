from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import api_router
from .db.database import crear_db

crear_db()

app = FastAPI(
    title="API Mi Proyecto",
    version="0.1.0"
)

# Habilitar CORS para el frontend (Vite/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL del frontend Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)