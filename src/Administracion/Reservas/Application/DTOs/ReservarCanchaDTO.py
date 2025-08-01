from pydantic import BaseModel
from datetime import datetime

class ReservarCanchaDTO(BaseModel):
    id: str
    fecha_hora: datetime
    duracion: int
    cancha_id: str
    jugador_id: str