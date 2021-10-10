from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional [str]
    userId: str
    nivel: str
    fecha: str
    hora: str
    descripcion: str
