from dataclasses import dataclass
from datetime import datetime

@dataclass
class ReservarCanchaDTO:
    id_reserva: str
    fecha_hora: datetime
    duracion: int
    cancha_id: str