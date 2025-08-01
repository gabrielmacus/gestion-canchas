from dataclasses import dataclass
from pydantic import BaseModel, field_validator
from datetime import datetime, timedelta
import uuid

class ReservaDTO(BaseModel):
    id: str
    fecha_hora: datetime
    duracion: int
    cancha_id: str
    jugador_id: str 
    