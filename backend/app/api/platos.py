from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..models.models import Plato, PlatoRead
from ..db.database import get_session

router = APIRouter(prefix="/platos", tags=["platos"])

@router.get("/", response_model=List[PlatoRead])
def listar_platos(session: Session = Depends(get_session)):
    platos = session.exec(select(Plato)).all()
    return platos

@router.post("/", response_model=PlatoRead)
def crear_plato(plato: Plato, session: Session = Depends(get_session)):
    session.add(plato)
    session.commit()
    session.refresh(plato)
    return plato

@router.get("/{plato_id}", response_model=PlatoRead)
def obtener_plato(plato_id: int, session: Session = Depends(get_session)):
    plato = session.get(Plato, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    return plato

@router.put("/{plato_id}", response_model=PlatoRead)
def actualizar_plato(plato_id: int, datos: Plato, session: Session = Depends(get_session)):
    plato = session.get(Plato, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    plato.nombre = datos.nombre
    plato.descripcion = datos.descripcion
    plato.precio = datos.precio
    session.commit()
    session.refresh(plato)
    return plato

@router.delete("/{plato_id}")
def eliminar_plato(plato_id: int, session: Session = Depends(get_session)):
    plato = session.get(Plato, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    session.delete(plato)
    session.commit()
    return {"ok": True}