from pydantic import BaseModel
from typing import Optional

class JugadorDTO(BaseModel):
    id: str
    nombre: str
    apellido: str
    telefono: str
    email: Optional[str] = None
