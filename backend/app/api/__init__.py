from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "¡Bienvenido a la API de Mi Proyecto!"}