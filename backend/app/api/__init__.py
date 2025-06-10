from fastapi import APIRouter
from .platos import router as platos_router
from .ordenes import router as ordenes_router
from .pagos import router as pagos_router

api_router = APIRouter()
api_router.include_router(platos_router)
api_router.include_router(ordenes_router)
api_router.include_router(pagos_router)

@api_router.get("/")
def root():
    return {"message": "¡Bienvenido a la API de Mi Proyecto!"}