from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..models.models import Orden, Plato, OrdenRead, PlatoRead, OrdenPlatoLink
from ..db.database import get_session

router = APIRouter(prefix="/ordenes", tags=["ordenes"])

@router.get("/", response_model=List[OrdenRead])
def listar_ordenes(session: Session = Depends(get_session)):
    ordenes = session.exec(select(Orden)).all()
    return ordenes

@router.post("/", response_model=OrdenRead)
def crear_orden(orden: Orden, session: Session = Depends(get_session)):
    session.add(orden)
    session.commit()
    session.refresh(orden)
    return orden

@router.get("/{orden_id}", response_model=OrdenRead)
def obtener_orden(orden_id: int, session: Session = Depends(get_session)):
    orden = session.get(Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden

@router.put("/{orden_id}", response_model=OrdenRead)
def actualizar_orden(orden_id: int, datos: Orden, session: Session = Depends(get_session)):
    orden = session.get(Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    orden.pagada = datos.pagada
    session.commit()
    session.refresh(orden)
    return orden

@router.delete("/{orden_id}")
def eliminar_orden(orden_id: int, session: Session = Depends(get_session)):
    orden = session.get(Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    session.delete(orden)
    session.commit()
    return {"ok": True}