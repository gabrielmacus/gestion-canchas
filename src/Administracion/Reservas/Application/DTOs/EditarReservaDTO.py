
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class EditarReservaDTO(BaseModel):
    fecha_hora: Optional[datetime] = None
    duracion: Optional[int] = None
    cancha_id: Optional[str] = None
    jugador_id: Optional[str] = None