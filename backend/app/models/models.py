from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# --- Tabla de relación ---
class OrdenPlatoLink(SQLModel, table=True):
    orden_id: Optional[int] = Field(default=None, foreign_key="orden.id", primary_key=True)
    plato_id: Optional[int] = Field(default=None, foreign_key="plato.id", primary_key=True)

# --- MODELOS BASE ---
class PlatoBase(SQLModel):
    nombre: str
    descripcion: str
    precio: float

class OrdenBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.utcnow)
    pagada: bool = False

# --- MODELOS DE BASE DE DATOS ---
class Plato(PlatoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ordenes: List["Orden"] = Relationship(back_populates="platos", link_model=OrdenPlatoLink)

class Orden(OrdenBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platos: List[Plato] = Relationship(back_populates="ordenes", link_model=OrdenPlatoLink)

class Pago(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    orden_id: int = Field(foreign_key="orden.id")
    monto: float
    fecha: datetime = Field(default_factory=datetime.utcnow)

# --- MODELOS DE RESPUESTA (para evitar ciclos en la API) ---
class PlatoRead(PlatoBase):
    id: int

class OrdenRead(OrdenBase):
    id: int
    platos: List[PlatoRead] = []

class PagoRead(SQLModel):
    id: int
    orden_id: int
    monto: float
    fecha: datetime