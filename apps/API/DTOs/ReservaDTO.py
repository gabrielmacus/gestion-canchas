from dataclasses import dataclass
from datetime import datetime

@dataclass
class ReservaDTO:
    id: str
    fecha_hora: datetime
    duracion: int
    cancha_id: str
    jugador_id: str 