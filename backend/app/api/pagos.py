from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..models.models import Pago, PagoRead
from ..db.database import get_session

router = APIRouter(prefix="/pagos", tags=["pagos"])

@router.get("/", response_model=List[PagoRead])
def listar_pagos(session: Session = Depends(get_session)):
    return session.exec(select(Pago)).all()

@router.post("/", response_model=PagoRead)
def crear_pago(pago: Pago, session: Session = Depends(get_session)):
    session.add(pago)
    session.commit()
    session.refresh(pago)
    return pago

@router.get("/{pago_id}", response_model=PagoRead)
def obtener_pago(pago_id: int, session: Session = Depends(get_session)):
    pago = session.get(Pago, pago_id)
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return pago

@router.delete("/{pago_id}")
def eliminar_pago(pago_id: int, session: Session = Depends(get_session)):
    pago = session.get(Pago, pago_id)
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    session.delete(pago)
    session.commit()
    return {"ok": True}