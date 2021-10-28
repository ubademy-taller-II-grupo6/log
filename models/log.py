from pydantic import BaseModel
from typing import Optional


class Entry(BaseModel):
    id: Optional[str]
    userId: str
    nivel: str
    fecha: str
    hora: str
    descripcion: str
