from pydantic import BaseModel
from typing import Optional


class Entry(BaseModel):
    userId: str
    fecha: str
    hora: str
    nivel: str
    descripcion: str
